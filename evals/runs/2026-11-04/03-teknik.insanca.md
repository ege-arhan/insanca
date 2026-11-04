# Çıktı 3 — Teknik dokümantasyon

Önbellek katmanı veritabanı yükünü azaltır, yanıt sürelerini kısaltır. Üç seviyesi var.

Birinci seviye istek içinde yaşıyor ve aynı döngüde tekrar eden sorguları yakalıyor. İkinci seviye Redis, süreçler arasında paylaşılıyor. Üçüncü seviye kalıcı depo, yalnızca yazma işleminden sonra güncelleniyor.

Geçersizleştirmeyi yanlış kurarsan veri tutarsızlaşır. Bu yüzden yazma işlemleri tek kuyruktan geçiyor, ilgili anahtarlar atomik olarak siliniyor.

```python
cache.set("user:42", payload, ttl=300)
```

TTL varsayılanı 300 saniye ve ortam değişkeninden okunuyor, yoğun uç noktalarda bu değeri düşür. İsabet oranı metriklerini izle. 300 saniye her uç nokta için doğru cevap değil.
