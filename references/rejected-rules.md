# Reddedilen kurallar

Buraya, denendiği halde **elenen** kurallar yazılır. Sebep basit: aksi halde İngilizce sezgiler Türkçe kural diye paketlenir. Yeni kural eklemeden önce bu dosyayı oku.

## R1 — "Em dash her zaman yasak"

**Öneri:** `—` gördüğün her yerde virgül/nokta koy.
**Neden elendi:** İnsan Türkçesinde em dash ölçüldü: **0,98/1000 kelime**, yani yasak değil, seyrek. Em dash yasağı ABD editoryal normudur; Türkçeye ithal.
**Yerine gelen kural:** §23 (S3, seyrekliği ölç). Asıl ithal işaret em dash değil, iki bağımsız cümleyi `;` ile bağlayan **noktalı virgül köprüsü** (§38).

## R2 — "`-mektedir` gördüğün yerde kes"

**Öneri:** Bütün `-mektedir/-maktadır` eklerini `-yor`a çevir.
**Neden elendi:** Bu ek akademik, hukuki ve resmî register'da **standarttır**; kesmek metni bozar. Yalnızca blog/gündelik register'da kusurdur ve orada da sinyal tek ek değil **yoğunluktur**.
**Yerine gelen kural:** §1 (S1 blog/gündelik, S3 akademik/resmî) + `--register` bayrağı. Ölçüm: insan sohbet korpusunda 0,00/1000, blog metninde 2+/paragraf ise düzelt.

## R3 — "İngilizce sözcük listesini çevir, o kelimeleri yasakla"

**Öneri:** `crucial → kritik`, `robust → sağlam`, `showcase → sergile`, `delve → derinlemesine incele` gibi listeyi Türkçeye çevirip yasak ilan et.
**Neden elendi:** Türkçe eklemeli bir dil; kelime düzeyinde karşılık tutmuyor. "kritik" insan yazısında da sık, "sağlam" teknik metinde standart, "derinlemesine" edebî. Kelime listesi yanlış pozitif üretir; gerçek iz **yapıda** (§3, §19, §35).
**Yerine gelen kural:** Yalnız sözcük değil kalıp düzeyinde eşleşme (`büyük önem taşımaktadır`, `kritik rol oynamaktadır` §11).

## R4 — "`sadece ... değil` yapısını yakalayan dedektör `değil` ile eşleşsin"

**Öneri:** Basit `değil` araması yap.
**Neden elendi:** Türkçede `değil` günlük dilin en sık sözcüklerinden biri ("öyle değil", "yok değil"). Basit arama %90 yanlış pozitif. Ayrıca `-DIr` kopulasıyla karışıyor.
**Yerine gelen kural:** §14 yalnız `sadece/yalnızca … değil … aynı zamanda` üçlüsünü arar; tek `değil` serbest.

## R5 — "`bir` gördüğün yerde sil"

**Öneri:** Artikel olmayan dilde `bir` fazlalıktır, sil.
**Neden elendi:** `bir` Türkçede belirsizlik ve sayı bildirir; silmek anlam bozar ("bir gün" ≠ "gün"). Ayrıca insan korpusunda `bir` 14,3/1000 kelime, yani sanıldığı kadar nadir değil.
**Yerine gelen kural:** §37 (S2): yalnız soyut isim kalıbında (`bir çözüm sunar`) düzelt.

## R6 — "Ritim için cümle uzunluğu varyansını (burstiness) hedefle"

**Öneri:** Cümle uzunluklarının standart sapmasını artır.
**Neden elendi:** Türkçede kelime sırası serbest; uzunluk varyansı doğal olarak yüksek çıkar, sinyal gürültüye gömülür. Ölçüt **hece sayısı** ve **yüklem konumu** olmalı.
**Yerine gelen kural:** §18 ve §34 ölçü notu.

## R7 — "Her cümleyi devrik yap"

**Öneri:** Devrik cümle insan işaretidir, hepsini devrik kur.
**Neden elendi:** İnsan metninde yüklem-sonlu cümle oranı %32–36; yani cümlelerin kabaca üçte ikisi devrik/eksiltili ama üçte biri düz. Hepsi devrik olursa metin tuhaf bir "konuşma taklidi" olur ve aşırı düzeltme kapısını açar.
**Yerine gelen kural:** §29: paragraf başına 1–3 devrik, gerisi doğal.

## R8 — "Kalın etiketli madde listelerini her zaman nesre çevir"

**Öneri:** `**Hız:** …` biçimini yasakla.
**Neden elendi:** Teknik dokümantasyonda kalın etiket işlevseldir, referans metinde standarttır. Kusur değil, register meselesi.
**Yerine gelen kural:** §24 (S2, teknik register'da devre dışı).

## R9 — "Sohbet artıklarını sil, ama kapanış nezaketini koru"

**Öneri:** "Umarım yardımcı olmuştur"u tut, çünkü insan da yazıyor.
**Neden elendi:** Bu cümle sohbet arayüzünün artığıdır; metin kendi başına durması gerektiğinde anlamsızdır. Türkçe metinde %90 model işareti.
**Yerine gelen kural:** §27 (S1, istisnasız).

## R10 — "Alıntılardaki kalıpları da düzelt"

**Öneri:** Kalıp her yerde kalıptır, alıntıda da düzelt.
**Neden elendi:** Alıntı değiştirilirse metin yalan söyler. Kapsam dışı liste kesin.
**Yerine gelen kural:** Kapsam dışı span listesi (sayı, ad, tarih, alıntı, terim, kod, yasal metin).

---

## Karar veremediklerim (açık sorular)

- **Noktalı virgül.** Güvenilir insan taban çizgisi çıkarılamadı: korpustaki `;` büyük ölçüde CSS/stil parçalarından geliyor. §38 şimdilik S3 ve sezgisel. Ölçüm yapılınca güncellenecek.
- **Emoji.** Sosyal medya register'ında insan da emoji kullanıyor; blog'da kullanmıyor. §24 register'a bağlı bırakıldı, mutlak yasak değil.
- **`adeta`.** Edebî metinde doğal, blogda dolgu. Yalnız register kontrolüyle uygulanıyor (§13, S2).
