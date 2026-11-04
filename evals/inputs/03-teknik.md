# Test girdisi 3 — Teknik dokümantasyon

## Konu: Önbellekleme katmanı

Bu döküman, uygulamamızda kullanılan önbellekleme katmanını açıklamak amacıyla hazırlanmıştır. Önbellek katmanı, veritabanı yükünü azaltmak ve yanıt sürelerini iyileştirmek için tasarlanmıştır.

Mimari üç seviyeden oluşmaktadır. Birinci seviye, istek bazında çalışan in-memory önbellektir ve aynı istek döngüsü içinde tekrarlanan sorguları engeller. İkinci seviye, dağıtık Redis katmanıdır; süreçler arası paylaşımı sağlamaktadır. Üçüncü seviye ise kalıcı depolamadır ve yalnızca yazma işlemlerinden sonra güncellenmektedir.

Önemli nokta, önbellek geçersizleştirme stratejisidir. Yanlış kurgulanmış bir geçersizleştirme mekanizması, veri tutarsızlığına yol açabilmektedir. Bu nedenle, yazma işlemleri merkezi bir kuyruk üzerinden sıralanmakta ve ilgili anahtarlar atomik olarak temizlenmektedir.

Kullanım için örnek:

```python
cache.set("user:42", payload, ttl=300)
```

Yapılandırma değerleri ortam değişkenleri üzerinden okunmaktadır. Varsayılan TTL değeri 300 saniyedir; yüksek trafikli uç noktalar için bu değerin düşürülmesi önerilmektedir. Ayrıca, gözlemlenebilirlik açısından isabet oranı metriklerinin izlenmesi büyük önem taşımaktadır.
