#!/usr/bin/env python3
"""Sohbet arşivinden temiz insan Türkçesi taban çizgisi çıkarır.

Kullanım: python3 scripts/corpus_human.py [ARSIV_DIZINI] [-o data/human-baseline.json]
"""
import json
import re
import sys
from pathlib import Path

ARCHIVE = Path.home() / ".claude/codex-import/chats"
TR_CHARS = set("çğıöşüÇĞİÖŞÜ")
STOP = {"bir", "ve", "bu", "da", "de", "için", "ile", "çok", "ama", "daha", "gibi", "olarak",
        "var", "yok", "ben", "sen", "o", "biz", "siz", "ki", "mi", "ne", "her", "sonra"}
CODE = re.compile(r"```.*?```", re.S)
NOISE = re.compile(r"^(\[local|#|[-*]{2,}|<|/[A-Za-z])")
BAD = re.compile(r"[{}|<>/=]|\]\(|\bhttp")
NOISY_PHRASES = ("Files mentioned by the user", "My request for Codex", "conversation ID",
                 "Project folder", "Historical transcript")


def sections(text, tag):
    return re.split(rf"^## {tag}\s*$", text, flags=re.M)[1:]


def clean(block):
    block = CODE.sub(" ", block)
    block = re.sub(r"`[^`\n]+`", " ", block)
    block = re.sub(r"https?://\S+", " ", block)
    lines = [ln for ln in block.splitlines() if not NOISE.match(ln.strip())]
    return " ".join(lines)


def turkish_ok(text):
    words = re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşü]+", text)
    if len(words) < 12:
        return False
    tr = sum(1 for w in words if TR_CHARS & set(w)) / len(words)
    stop = sum(1 for w in words if w.lower() in STOP) / len(words)
    ascii_long = sum(1 for w in words if len(w) > 4 and not (TR_CHARS & set(w)))
    return tr >= 0.06 and stop >= 0.10 and ascii_long / len(words) < 0.45


def denom(word):
    """Türkçe küçük harf: İ->i, I->ı."""
    return word.replace("İ", "i").replace("I", "ı").lower()


def stats(records):
    text = "\n".join(records)
    w = len(re.findall(r"\S+", text))
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    lens = [len(re.findall(r"\S+", s)) for s in sents]
    lens.sort()
    strong = re.compile(r"\w+(yor|dı|di|du|dü|tı|ti|tu|tü|mış|miş|muş|müş|acak|ecek|mekte|makta|"
                        r"maktadır|mektedir|malı|meli|yız|yiz|sunuz|sünüz|dır|dir|dur|dür)$")
    bare_r = re.compile(r"[a-zçğıöşü]{4,}r$")
    body = [re.sub(r"[.!?]+$", "", s).strip().split()[-1].lower() for s in sents if s.split()]
    body = [re.sub(r"^[^\wçğıöşü]+|[^\wçğıöşü]+$", "", w) for w in body]
    hi = sum(1 for w in body if strong.fullmatch(w) or bare_r.fullmatch(w))
    lo = sum(1 for w in body if strong.fullmatch(w))
    final_verb = hi / max(1, len(body))
    def per1k(n): return round(n / max(1, w) * 1000, 2)
    return {
        "records": len(records), "words": w, "sentences": len(sents),
        "words_per_record": round(w / max(1, len(records)), 1),
        "words_per_sentence_mean": round(w / max(1, len(sents)), 2),
        "words_per_sentence_median": lens[len(lens) // 2] if lens else 0,
        "pct_sentences_gt40w": round(sum(1 for x in lens if x > 40) / max(1, len(sents)) * 100, 2),
        "pct_sentences_le8w": round(sum(1 for x in lens if x <= 8) / max(1, len(sents)) * 100, 2),
        "sentence_final_verb_pct": round(final_verb * 100, 2),
        "sentence_final_verb_pct_lo": round(lo / max(1, len(body)) * 100, 2),
        "punct_per_1k": {
            "em_dash": per1k(text.count("—")), "en_dash": per1k(text.count("–")),
            "semicolon": per1k(text.count(";")), "colon": per1k(text.count(":")),
            "paren": per1k(text.count("(")), "ellipsis": per1k(text.count("…") + text.count("...")),
            "question": per1k(text.count("?")), "exclaim": per1k(text.count("!")),
            "curly_quote": per1k(text.count("“") + text.count("”")),
        },
        "suffix_per_1k": {
            "yor": per1k(len(re.findall(r"\b\w+yor\b", text))),
            "mekte_makta": per1k(len(re.findall(r"\b\w+(mekte|makta|mektedir|maktadır)\b", text))),
            "mis_mush": per1k(len(re.findall(r"\b\w+(mış|miş|muş|müş)\w*\b", text))),
        },
        "dolgu_per_1k": {k: per1k(len(re.findall(rf"\b{k}\b", denom(text))))
                         for k in ("yani", "işte", "hani", "bence", "sanırım", "galiba",
                                   "açıkçası", "tabii", "bir", "aslında")},
    }


def main():
    archive = Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else ARCHIVE
    out = Path("data/human-baseline.json")
    if "-o" in sys.argv:
        out = Path(sys.argv[sys.argv.index("-o") + 1])
    records, seen = [], set()
    for f in sorted(archive.glob("*.md")):
        try:
            raw = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if any(p in raw[:800] for p in NOISY_PHRASES) is False:
            continue
        for block in sections(raw, "User"):
            t = clean(block).strip()
            if not turkish_ok(t) or not 40 <= len(re.findall(r"\S+", t)) <= 400:
                continue
            if BAD.search(t) or len(t.splitlines()) > 3:
                continue
            key = t[:120]
            if key in seen:
                continue
            seen.add(key)
            records.append(t)
    res = {"source": str(archive), "clean_records": len(records), "baseline": stats(records)}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(res["baseline"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
