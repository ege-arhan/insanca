#!/usr/bin/env python3
"""Katmanlı doğrulama: skor ayrımı ve yanlış pozitif kontrolü.

    python3 scripts/selftest.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tells import measure  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def score(text, register="blog"):
    return measure(text, register)["score"]


AI_INPUTS = sorted((ROOT / "evals/inputs").glob("*.md"))
HUMAN_OUT = sorted((ROOT / "evals/runs/2026-11-04").glob("*.insanca.md"))


def main():
    assert AI_INPUTS and HUMAN_OUT, "eval dosyaları eksik"
    ai = [(f.name, score(f.read_text(encoding="utf-8"))) for f in AI_INPUTS]
    hu = [(f.name, score(f.read_text(encoding="utf-8"))) for f in HUMAN_OUT]
    for name, s in ai:
        assert s >= 60, f"YZ girdisi düşük skor aldı: {name} {s}"
    for name, s in hu:
        assert s <= 40, f"insanlaştırılmış çıktı yüksek skor aldı: {name} {s}"
    assert min(s for _, s in ai) > max(s for _, s in hu), "sınıflar ayrışmıyor"

    # yanlış pozitif: temiz insan Türkçesi yüksek skor almamalı
    temiz = ("Bugün eve erken gittim. Yolda eski bir arkadaşa rastladım, "
             "iki saat konuştuk. Zaman nasıl geçti anlamadım. Eve vardığımda "
             "yemek soğumuştu ama umurumda değildi. Yarın da ararım belki.")
    assert score(temiz) < 22, f"temiz metin yanlış pozitif: {score(temiz)}"

    # register: kurumsal metinde -mektedir ceza almamalı
    kurumsal = ("Yönetim Kurulu kararıyla yeni politika 1 Ocak 2026 itibarıyla yürürlüğe girmektedir. "
                "Başvurular ilgili birime yapılmaktadır. Süreç boyunca mevzuat hükümleri uygulanmaktadır. "
                "Talepler değerlendirilmektedir.")
    assert score(kurumsal, "resmi") < score(kurumsal, "blog"), "register farkı çalışmıyor"

    print("YıZ girdileri :", ", ".join(f"{n}={s}" for n, s in ai))
    print("Çıktılar      :", ", ".join(f"{n}={s}" for n, s in hu))
    print("Temiz metin   :", score(temiz))
    print("OK — tüm kontroller geçti")


if __name__ == "__main__":
    main()
