#!/usr/bin/env python3
"""insanca — Türkçe metin "makine kokusu" skoru.

Kullanım:
    python3 scripts/tells.py METIN.md
    python3 scripts/tells.py --register blog evals/inputs/01-blog.md
    echo "metin" | python3 scripts/tells.py -
    python3 scripts/tells.py --json METIN.md

Skor 0–100: 0 temiz insan yazısı, 100 yoğun YZ metni.
Taban çizgisi data/human-baseline.json (175 kayıt, 21.401 kelime, Türkçe sohbet).
"""
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE_FILE = ROOT / "data/human-baseline.json"

# İnsan taban çizgisi (ölçülmüş, data/human-baseline.json ile aynı)
BASE = {"words_per_sentence_median": 12, "pct_short": 28.1, "pct_long": 3.5,
        "mekte_makta": 0.0, "em_dash": 0.98, "paren": 1.31}

# (numara, şiddet, regex, ağırlık, register istisnası)
TELLS = [
    ("§1", "S1", r"\b\w+(mektedir|maktadır)\b", 1.0, {"akademik", "resmi"}),
    ("§2", "S1", r"\b\w+(ilmektedir|ılmaktadır|ulmaktadır|ülmektedir)\b", 1.2, None),
    ("§3", "S2", r"\b(gerçekleştir|sağla|sun|oluştur|icra et)\w*\b", 0.5, None),
    ("§4", "S2", r"\b\w+(nin|nın|in|ın) \w+(süreç|yaklaşım|sistem|yapı)\w*(ler|lar)\w*(in|ın|nin|nın) "
                 r"\w+(si|sı|i|ı)\b", 0.6, None),
    ("§5", "S2", r"\b\w+(mek|mak), \w+(mek|mak)( ve \w+(mek|mak))?\b", 0.6, None),
    ("§6", "S1", r"\bbu (bağlamda|doğrultuda|çerçevede|kapsamda|noktada|süreçte|itibarla)\b", 1.5, None),
    ("§7", "S1", r"^(ayrıca|bununla birlikte|buna ek olarak|öte yandan|dolayısıyla|böylece|"
                 r"bu nedenle|sonuç olarak|özetle|kısacası|özet olarak)\b", 1.2, None),
    ("§8", "S1", r"\b(yanlış anlaşılmasın|anlamına gelmez|belirtmek gerekir ki|kuşkusuz|elbette|"
                 r"hiç şüphesiz|şüphesiz)\b", 1.2, None),
    ("§9", "S1", r"\b(unutulmamalıdır|unutmayın|altını çizmek gerekir|dikkat edilmesi gereken)\b", 1.5, None),
    ("§10", "S1", r"\b(şöyle düşünün|hayal edin|hadi birlikte|gelin birlikte|işte burada|"
                  r"devreye giriyor|peki bu ne)\b", 1.3, None),
    ("§11", "S1", r"\b(büyük önem taşı|kritik (bir )?rol oyna|hayati önem|temelini oluştur|"
                  r"vazgeçilmez|kilit (faktör|rol|unsur)|kilometre taşı)", 1.5, None),
    ("§12", "S1", r"\b(zengin bir \w+ sun|geniş bir yelpaze|sayısız fırsat|eşsiz bir deneyim|"
                  r"potansiyel (vaat|sun)|ufuk açıcı)", 1.4, None),
    ("§13", "S2", r"\b(aslında mesele|işin özü|gerçek soru|temelde|esasen|bir anlamda|adeta|"
                  r"sanki|bir nevi)\b", 0.6, None),
    ("§14", "S1", r"\b(sadece|yalnızca) .{0,60}(değil).{0,40}(aynı zamanda|ayrıca)\b", 1.3, None),
    ("§16", "S1", r"\b(uzmanlara göre|araştırmalar göster|bilim insanları|sektör raporları|"
                  r"birçok kaynak|genel kabul görmüş)\b", 1.3, None),
    ("§17", "S2", r"\b(zengin kültürel miras|büyüleyici|göz alıcı|kusursuz|ideal çözüm|"
                  r"yenilikçi ve sürdürülebilir|mükemmeliyet)\b", 0.8, None),
    ("§19", "S1", r"\b(\w+ya sahip|\w+e sahip|ihtiyaç duyul|etkili bir şekilde|verimli bir şekilde|"
                  r"başarılı bir şekilde|için tasarlanmıştır)", 1.2, None),
    ("§21", "S2", None, 0.5, None),
    ("§24", "S2", r"(\*\*[^*\n]{2,40}:\*\*|[\U0001F300-\U0001FAFF\u2190-\u21FF])", 0.7, {"teknik"}),
    ("§26", "S2", r"\bbu (yazıda|rehberde|bölümde|dökümanda)\b.{0,60}\b(ele alın|incelen|amaçla|yer al)", 1.0, None),
    ("§27", "S1", r"\b(umarım (bu|yardımcı)|başka (bir )?soru|keyifli okumalar|iyi çalışmalar|"
                  r"harika soru|işte karşınızda)\b", 1.5, None),
    ("§28", "S1", r"\b(kesin bilgi bulunmamakla|bilgilerim .{0,20}itibariyle|tahmin edilmektedir|"
                  r"olduğu düşünülmektedir|olduğu değerlendirilmektedir)\b", 1.4, None),
    ("§35", "S2", r"\b\w+(dığı|diği|duğu|düğü) (belirtilen|görülen|ifade edilen|öngörülen|bilinen)\b", 0.8, None),
    ("§36", "S2", r"\btarafından\b", 0.9, None),
    ("§37", "S2", r"\bbir (çözüm|yaklaşım|süreç|anlayış|strateji|deneyim|fırsat|adım)\b", 0.4, None),
    ("§38", "S3", r";\s", 0.3, None),
]

FORMAL = {"resmi", "akademik"}


def denom(t):
    return t.replace("İ", "i").replace("I", "ı").lower()


def measure(text, register="blog"):
    # yalnız nesir ölçülür: kod bloğu ve başlıklar metrik dışı
    prose = re.sub(r"```.*?```", " ", text, flags=re.S)
    prose = "\n".join(l for l in prose.splitlines() if not l.lstrip().startswith("#"))
    text = prose.strip() or text
    t = denom(text)
    words = re.findall(r"\S+", text)
    w = max(1, len(words))
    sents = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    lens = [len(s.split()) for s in sents] or [0]
    body = [re.sub(r"[^\wçğıöşü]", "", s.split()[-1].lower()) for s in sents if s.split()]
    strong = re.compile(r"\w+(yor|dı|di|du|dü|tı|ti|tu|tü|mış|miş|muş|müş|acak|ecek|malı|meli|dır|dir)$")

    def per1k(n):
        return n / w * 1000

    m = {
        "words": len(words), "sentences": len(sents),
        "median_sentence": sorted(lens)[len(lens) // 2],
        "pct_short": round(sum(1 for x in lens if x <= 8) / len(lens) * 100, 1),
        "pct_long": round(sum(1 for x in lens if x > 40) / len(lens) * 100, 1),
        "verb_final_pct": round(sum(1 for x in body if strong.fullmatch(x)) / max(1, len(body)) * 100, 1),
        "em_dash": round(per1k(text.count("—") + text.count("–")), 2),
        "paren": round(per1k(text.count("(")), 2),
        "mekte_makta": round(per1k(len(re.findall(r"\b\w+(mektedir|maktadır)\b", t))), 2),
    }
    hits, total = [], 0.0
    for num, sev, rx, weight, exc in TELLS:
        if rx and exc and register in exc:
            continue
        if rx is None:  # §21 uzun cümle
            n = max(0, m["pct_long"] - BASE["pct_long"])
            total += weight * n / 10
            if n > 0:
                hits.append({"no": num, "sev": sev, "count": round(n, 1), "note": "% uzun cümle fazlası"})
            continue
        flags = re.M | re.I
        n = len(re.findall(rx, t, flags)) if rx.startswith("^") else len(re.findall(rx, t, flags))
        if n:
            total += weight * math.log1p(n) * 2.2
            hits.append({"no": num, "sev": sev, "count": n})
    # yokluk sinyalleri
    absent = []
    if m["median_sentence"] > BASE["words_per_sentence_median"] + 4:
        absent.append("uzun cümle (medyan %s)" % m["median_sentence"])
    if m["pct_short"] < BASE["pct_short"] / 2:
        absent.append("kısa cümle yok (%%%.0f)" % m["pct_short"])
    if m["verb_final_pct"] > 65:
        absent.append("devrik cümle yok (yüklem-sonlu %%%.0f)" % m["verb_final_pct"])
    if m["pct_short"] > 55 or m["median_sentence"] < 6:
        absent.append("aşırı kopuk cümle (kısa %%%.0f, medyan %s)" % (m["pct_short"], m["median_sentence"]))
    total += 1.5 * len(absent)
    score = round(min(100.0, 100 * (1 - math.exp(-total / 9.0))), 1)
    verdict = ("insan yazısı gibi" if score < 22 else "büyük olasılıkla insan" if score < 42
               else "şüpheli" if score < 68 else "makine kokusu yoğun")
    return {"register": register, "score": score, "verdict": verdict, "metrics": m,
            "hits": sorted(hits, key=lambda h: h["sev"]), "absent_signals": absent}


def main():
    args = [a for a in sys.argv[1:]]
    as_json = "--json" in args
    args = [a for a in args if a not in ("--json",)]
    register = "blog"
    if "--register" in args:
        i = args.index("--register")
        register, args = args[i + 1], args[:i] + args[i + 2:]
    if not args:
        print(__doc__)
        return 1
    text = sys.stdin.read() if args[0] == "-" else Path(args[0]).read_text(encoding="utf-8")
    res = measure(text, register)
    if as_json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    m = res["metrics"]
    print(f"{args[0]}  register={register}")
    print(f"SKOR {res['score']}/100 — {res['verdict']}")
    print(f"kelime={m['words']} cümle={m['sentences']} medyan={m['median_sentence']} "
          f"kısa%= {m['pct_short']} uzun%={m['pct_long']} yüklem-sonlu%={m['verb_final_pct']} "
          f"-mektedir/1k={m['mekte_makta']} em-dash/1k={m['em_dash']}")
    if res["hits"]:
        print("İZLER: " + ", ".join(f"{h['no']}({h['sev']})x{h['count']}" for h in res["hits"]))
    if res["absent_signals"]:
        print("YOKLUK: " + "; ".join(res["absent_signals"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
