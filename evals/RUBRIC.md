# Hakem formu (kör değerlendirme)

Her metin için iki sürüm görürsün: **A** ve **B** (hangisinin insanlaştırılmış olduğu söylenmez). 1–5 puan ver.

## Puanlama

| Kriter | Ne ölçüyor | 1 | 5 |
|---|---|---|---|
| Doğallık | "Bunu bir Türk yazar mı yazdı?" | bariz makine | insan eli değmiş |
| Akıcılık | Cümle bağlantıları, ritim, devrik yapı | kütük, tek düze | doğal ritim |
| Anlam koruma | Bilgi kaybı / uydurma ekleme | bilgi kaybı var | birebir sadık |
| Ses | Kişilik, tutum, kayıtsızlık değil | jenerik | yazara ait |
| Kalıp temizliği | Türkçe LLM kalıpları | kalıp dolu | temiz |

## Kayıt

```
metin_no | kazanan (A/B/berabere) | doğallık | akıcılık | anlam | ses | kalıp | not
```

Ek olarak tek soru: **"Hangisi Türkçe LLM çıktısı gibi kokuyor ve neden?"** — buradaki cevaplar skill'e yeni kural olarak geri yazılır.

## Körleme

A/B sırası her metinde rastgele. Sıra `evals/runs/<tarih>/sirali.md` dosyasında tutulur, puanlama bitene kadar açılmaz.
