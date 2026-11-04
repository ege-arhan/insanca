# 02 — Türkçe YZ Metni İşaretleri (kural kitabı taslağı)

Amaç: "makine yazmış gibi duran" Türkçeyi ayırt edip kurala çevirmek. Her madde: yüzey işaretleri → neden YZ kokuyor → önce/sonra.

**Yöntem ve güven notu.** Bu oturumda arama API'si yoktu (`DEEPSEEK_API_KEY` yok); kaynaklara DuckDuckGo HTML proxy'si ve doğrudan `web_fetch` ile ulaşıldı. Dilbilgisi maddeleri ansiklopedik kaynaklarla, işaret listesinin bir kısmı Türkçe YZ-dedektörü şirketlerinin yayınlarıyla doğrulandı. Sıklık iddiaları (`adeta`, em dash, "-dir" yoğunluğu) **gözlem**dir, ölçülmüş korpus değildir — kural yazarken bunları "yüksek olasılık" diye işaretle.

---

## Bölüm 0 — Dilbilgisi zemini (yeniden yazım için şart)

1. **SOV ve serbest sıra.** Türkçe yüklem sonda (Ö-N-Y). Ama sıra serbesttir; değişen sıra **vurguyu** taşır: yüklemden hemen önceki öğe vurgulu. "Kitabı Ali okudu" ≠ "Ali kitabı okudu". YZ çoğu zaman tek sırayı (düz SOV) tekrarlar; insan vurgu için sıra oynatır.
2. **Devrik cümle doğal, hata değil.** Yüklemi sonda olmayan cümle. Edebiyat, vurgu ve "pratik amaç" için kullanılır; bozuk cümle sayılmaz ([Devrik cümle](https://tr.wikipedia.org/wiki/Devrik_c%C3%BCmle)). Konuşma Türkçesinin bel kemiği. YZ neredeyse hiç devrik kurmaz — en güçlü yapısal sinyallerden biri.
3. **Eklemeli dil, ek yığılması.** Anlam ekle gelir: `yap-tır-ıl-a-bil-mek`. YZ bunu abartıp edilgen + ettirgen zinciri kurar ("gerçekleştirilebilmektedir"); insan çoğu zaman çatıyı sadeleştirir ("yapılabiliyor").
4. **Artikel yok.** "a/the" karşılığı yok; belirsizlik `bir`, belirlilik nesne durumu (`-ı`) veya bağlamla. YZ İngilizceden çevirirken gereksiz `bir` serper ("bir çözüm sunar").
5. **Ünlü uyumu.** Büyük uyum (kalınlık-incelik) ve küçük uyum (düzlük-yuvarlaklık) ek seçimini belirler ([Büyük ünlü uyumu](https://tr.wikipedia.org/wiki/B%C3%BCy%C3%BCk_%C3%BCnl%C3%BC_uyumu)). YZ uyumu bozmaz ama uyumsuz yabancı kökleri ("check etmek", "update'lemek") yanlış ekler; insan ya Türkçesini kullanır ya da argo diye işaretler.
6. **`-dir/-dır` kopulası.** Geniş zaman/kesinlik bildirir; gündelik yazıda çoğu zaman **düşer**. Her cümleye `-dir` koymak ders kitabı/Resmî Gazete tonu verir. Akademik ve kurumsal metinde meşru, sohbette değil.
7. **`ki` bağlacı.** Bağlaç `ki` ayrı yazılır ("biliyorum ki"); sıfat `-ki` bitişik ("akşamki"). YZ `ki`'yi İngilizce "that" gibi gereksiz yerlerde kullanır ("Şu gerçek ki...").
8. **`de/da`.** Bağlaç ayrı ("ben de"), bulunma hâli bitişik ("evde"). YZ karıştırmaz; ama bağlaç `de`'yi İngilizce "also" gibi her cümleye yığar.
9. **Kişi ve kayıt.** `sen` (samimi), `siz` (kibar/resmî, aynı zamanda çoğul), `biz` (kurumsal "biz" veya yazar "biz"i). Türkçede kibar `siz` + `-mektedir` doğal eştir; `siz` + "kanka" veya `sen` + `-mektedir` çatlak verir. YZ'nin en sık hatası: gündelik soruya `siz` + tam resmî çekimle cevap.
10. **Görünüş (aspect).** `-yor` süreklilik/alışkanlık, `-r` genel doğru, `-mış` duyulan/çıkarım, `-dı` bitmiş. YZ her şeyi `-maktadır`a düzler; insan `-yor` ile anlatır, `-mış` ile rivayet eder.
11. **Tamlama zinciri.** Ad tamlaması Türkçede normaldir ([Tamlama](https://tr.wikipedia.org/wiki/Tamlama)); 3+ katman ("içerik üretim süreçlerinin optimizasyonuna yönelik yaklaşımlar") okunmaz olur, İngilizce isim kümesinin çevirisidir.
12. **Paragraf.** Modern web Türkçesi kısa: 2–4 cümle, sık satır sonu. Uzun dönemli (periodic) cümle edebî/akademik register'da var, blogda yok. YZ blog metninde akademik uzunluk + her paragrafta aynı 3 cümle ritmi kurar.

---

## Bölüm 1 — Sözcüksel işaretler

### 1. Geçiş dolgusu: "Bu bağlamda / Bu doğrultuda / Bu çerçevede"
- **Yüzey:** paragraf ya da cümle başında, ardından virgül.
- **Neden YZ:** "in this context / accordingly" kalıbının birebir karşılığı. Bağ kurmuyor, sadece paragrafı başlatıyor; içerik eklemiyor. İnsan ya "yani" der ya hiçbir şey demez.
- **Önce:** "Bu bağlamda, eğitimde dijital dönüşüm büyük önem taşımaktadır."
- **Sonra:** "Yani okullar dijitalleşiyor. Peki öğretmenin bunu kullanacak vakti var mı?"

### 2. Paragraf açılışı tekdüzeliği: "Ayrıca / Bununla birlikte / Öte yandan"
- **Yüzey:** her paragraf aynı bağlaçla açılıyor; metinde 3+ farklı bağlaç rotasyonu.
- **Neden YZ:** Bağlaçlar sıralama işareti gibi kullanılıyor, anlam ilişkisi kurmuyor. İnsan metninde bağlaç seyrektir, geçiş içerikle yapılır.
- **Önce:** "Ayrıca bu yöntem maliyeti düşürür. Bununla birlikte riskleri de beraberinde getirir."
- **Sonra:** "Yöntem ucuz. Riski var ama, onu da atlamayalım."

### 3. Kapanış kalıbı: "Sonuç olarak / Özetle / Kısacası"
- **Yüzey:** son paragraf bu üçünden biriyle başlar, ardından metnin özeti tekrarlanır.
- **Neden YZ:** Okul denemesi şablonu + "In conclusion". Söylenmişi tekrar eder; insan kapanışta yeni bir şey söyler ya da keser.
- **Önce:** "Sonuç olarak dijitalleşme kaçınılmazdır ve işletmeler bu dönüşüme ayak uydurmalıdır."
- **Sonra:** "Uyum sağlayan kalıyor, sağlamayan kapanıyor. Hepsi bu."

### 4. `-maktadır/-mektedir` enflasyonu
- **Yüzey:** gündelik/yarı resmî metinde bile her yüklem `-maktadır`; "-yor" neredeyse yok.
- **Neden YZ:** Modelin güvenli, "profesyonel" saydığı tek çekim. Türkçede bu ek resmî/kurumsal register'a aittir; sohbette yapaylık.
- **Önce:** "Bu özellik, kullanıcıların içerik üretmesini kolaylaştırmaktadır."
- **Sonra:** "Bu özellik içerik üretmeyi kolaylaştırıyor."

### 5. Şişirilmiş yüklem: "büyük önem taşımaktadır / kritik bir rol oynamaktadır / temelini oluşturmaktadır"
- **Yüzey:** `önem taşımak`, `rol oynamak`, `temelini oluşturmak`, `katkı sağlamak`.
- **Neden YZ:** İngilizce "plays a crucial role / forms the basis" kalıbının çevirisi; eylemi soyutlaştırır, bilgi vermez. Türkçede doğal karşılığı genelde düz fiil.
- **Önce:** "Veri güvenliği, işletmeler için kritik bir rol oynamaktadır."
- **Sonra:** "Veri güvenliği olmadan iş yürümez."

### 6. "Sadece ... değil, aynı zamanda ..."
- **Yüzey:** ikili vurgu; sık sık "yalnızca ... değil, aynı zamanda ..." varyantı.
- **Neden YZ:** "not only ... but also" şablonu. Türkçede bu yapı var ama nadir; YZ her paragrafta bir tane kurar.
- **Önce:** "Bu sadece bir araç değil, aynı zamanda bir düşünme biçimidir."
- **Sonra:** "Bu bir araç. Ama düşünme biçimini de değiştiriyor."

### 7. Zorunlu üçleme (triad)
- **Yüzey:** "X, Y ve Z" / "hem ... hem ... hem de"; her listede tam üç öğe.
- **Neden YZ:** Üçlü ritim "tam" durur, model bunu tercih eder. İnsan iki ya da dört verir, bazen tek.
- **Önce:** "Süreç; planlama, uygulama ve değerlendirme aşamalarından oluşmaktadır."
- **Sonra:** "Süreç üç adım: planla, uygula, ölç."

### 8. Süs zarfı: "adeta / adeta bir ... gibi / adeta ..."
- **Yüzey:** benzetmeyi güçlendirmek için `adeta`, `sanki`, `neredeyse` yığılması.
- **Neden YZ:** Benzetme zaten kurulu; zarf sadece süslüyor. Türkçede `adeta` edebî, gündelik yazıda komik durur. *(sıklık: gözlem)*
- **Önce:** "Yapay zekâ adeta bir dijital asistan gibi çalışır."
- **Sonra:** "Yapay zekâ dijital asistan gibi çalışıyor."

### 9. "Zengin bir ... sunar / potansiyel sunar"
- **Yüzey:** `sunmak` + soyut nesne: deneyim, içerik, olanak, perspektif.
- **Neden YZ:** "offers a rich ..." kalıbı. Ne sunulduğu belirsiz kalır; cümle bilgi taşımaz.
- **Önce:** "Platform, kullanıcılara zengin bir deneyim sunar."
- **Sonra:** "Platformda yapacak çok şey var."

### 10. Hafif fiiller: "gerçekleştirmek / sağlamak / sunmak"
- **Yüzey:** `analiz gerçekleştirmek`, `iyileştirme sağlamak`, `destek sunmak`.
- **Neden YZ:** İsim+genel fiil, İngilizce nominalleşmenin çevirisi. Türkçede tek fiil varken iki kelime kullanılır.
- **Önce:** "Analiz gerçekleştirilerek performans iyileştirmesi sağlanmıştır."
- **Sonra:** "Analizi yaptık, iki hatayı düzelttik."

### 11. İsim tamlaması zinciri
- **Yüzey:** üç ve daha fazla `-ın/-nin ... -sı` katmanı; "…na yönelik …", "…süreçlerinin …i".
- **Neden YZ:** İngilizce isim kümesinin ("AI-driven content production process optimization approaches") kelime kelime çevirisi; Türkçede soluk alacak yer kalmaz.
- **Önce:** "Yapay zekâ destekli içerik üretim süreçlerinin optimizasyonuna yönelik yaklaşımlar"
- **Sonra:** "Yapay zekâyla içerik üretimini hızlandırma yolları"

### 12. Tanım kalıbı: "X, Y'nin temelini oluşturur"
- **Yüzey:** "…nin temelini oluşturur / …nin ayrılmaz parçasıdır / …nin anahtarıdır".
- **Neden YZ:** Boş totoloji: güven ilişkinin temelidir, su hayatın kaynağıdır. Bilgi eklemez, sadece ağırlık verir.
- **Önce:** "Güven, her ilişkinin temelini oluşturur."
- **Sonra:** "Güven olmadan ilişki yürümez."

### 13. Didaktik hatırlatma: "unutulmamalıdır ki / belirtmek gerekir ki"
- **Yüzey:** cümle başında `ki`'li kalıp; ardından genel geçer doğru.
- **Neden YZ:** "it should not be forgotten that" — okuyucuya ders verme tonu. İnsan bunu ya hiç yazmaz ya parantezde itiraf eder.
- **Önce:** "Unutulmamalıdır ki her yatırımın bir riski vardır."
- **Sonra:** "Her yatırımda risk var. Kimse söylemiyor ama var."

### 14. `-e sahip olmak` (İngilizce calque)
- **Yüzey:** "yüksek performansa sahip", "geniş bir yelpazeye sahip", "… özelliğine sahiptir".
- **Neden YZ:** "has / is equipped with" çevirisi. Türkçede `sahip` fiili bu kadar sık değil; sıfat ya da düz fiil yeter.
- **Önce:** "Sistem, yüksek performansa sahip bir mimariye sahiptir."
- **Sonra:** "Sistemin mimarisi hızlı çalışıyor."

### 15. Değerlendirme klişesi: "önemlidir / gereklidir / kaçınılmazdır"
- **Yüzey:** cümle sonunda değerlendirme sıfatı; özne genelde eylem adı ("… yapmak önemlidir").
- **Neden YZ:** "it is important to ..." — hem calque hem boş. Kime, neden önemli, söylenmez.
- **Önce:** "Düzenli egzersiz yapmak önemlidir."
- **Sonra:** "Haftada üç gün yürüyün. Gerisi teferruat."

### 16. Aşırı hedge
- **Yüzey:** "bazı durumlarda", "çeşitli faktörlere bağlı olarak", "genellikle", "büyük ölçüde", "kısmen".
- **Neden YZ:** Risk almama. Cümle her şeyi söyler, hiçbir şey iddia etmez. İnsan iddia eder, yanılırsa düzeltir.
- **Önce:** "Bazı durumlarda, çeşitli faktörlere bağlı olarak sonuçlar değişebilmektedir."
- **Sonra:** "Sonuç kişiye göre değişiyor."

### 17. Soyut isim enflasyonu
- **Yüzey:** `unsur, faktör, süreç, yaklaşım, perspektif, bağlam, dinamik, olgu`.
- **Neden YZ:** İçerik yerine kategori. Metin dolgulu görünür, okununca boş çıkar.
- **Önce:** "Bu süreçte kültürel faktörlerin belirleyici bir unsur olduğu görülmektedir."
- **Sonra:** "Burada belirleyici olan kültür. Gerisi ayrıntı."

---

## Bölüm 2 — Sözdizimsel işaretler

### 18. Devrik cümle yokluğu
- **Yüzey:** her cümle yüklem-sonlu, düz SOV; metinde tek bir devrik yok.
- **Neden YZ:** Model "doğru" cümleyi tek şablonla kurar. Türkçede devrik, vurgu ve konuşma ritmi taşır; yokluğu metni ders kitabına çevirir.
- **Önce:** "Toplantıda alınan kararlar, tüm ekipler tarafından uygulanacaktır."
- **Sonra:** "Toplantıda karar aldık. Herkes uygulayacak, istisna yok."

### 19. Uzun dönemli cümle, çok yan cümle
- **Yüzey:** 40+ kelime, iki `-ken/-makla birlikte/-dığı` yan cümlesi, tek nokta.
- **Neden YZ:** Almanca/İngilizce akademik ritmin çevirisi. Türkçede yüklem sonda olduğu için yan cümle yığılınca okur yüklemi unutur.
- **Önce:** "Şirketlerin dijital dönüşüm süreçlerinde karşılaştıkları zorluklar çoğu zaman teknolojik altyapıdan kaynaklanmakla birlikte, asıl sorunun organizasyonel kültür olduğu görülmektedir."
- **Sonra:** "Şirketler dijitalleşemiyor. Sebep teknoloji değil, alışkanlık."

### 20. Em dash ve iki nokta süsü
- **Yüzey:** `—` ile araya açıklama; "üç şey — hız, güven, maliyet" düzeni.
- **Neden YZ:** İngilizce editoryal stil. Türkçede tire seyrek, açıklama iki nokta ya da noktayla verilir. *(sıklık: gözlem)*
- **Önce:** "Üç şey önemli — hız, güven ve maliyet."
- **Sonra:** "Üç şey önemli: hız, güven, maliyet."

### 21. İngilizce sözdizimi calque'i
- **Yüzey:** "… yapmak için … gerekir", "… yapmak önemlidir", "… olarak kabul edilir", edilgen `ihtiyaç duyulmaktadır`.
- **Neden YZ:** Çeviri grameri. Türkçe eylemi öne alır: "Bu sorun daha fazla veri istiyor."
- **Önce:** "Bu sorunu çözmek için daha fazla veriye ihtiyaç duyulmaktadır."
- **Sonra:** "Bu sorun daha fazla veri istiyor."

### 22. Kişi/kayıt karışması
- **Yüzey:** `siz` + `-mektedir` + "kanka/hadi" aynı metinde; ya da `sen` + tam resmî çekim.
- **Neden YZ:** Model register'ı sabit tutamaz; kibarlık ekler, samimiyeti taklit eder, ikisi çakışır.
- **Önce:** "Siz de görebileceğiniz üzere, sistem oldukça kullanışlıdır."
- **Sonra:** "Bak, sistem gerçekten kullanışlı."

### 23. Her cümlede `-dir` kesinliği
- **Yüzey:** üç kısa cümle, üçü de `-dır/-dir/-tir` ile bitiyor.
- **Neden YZ:** Ansiklopedi tonu. Gündelik yazıda kopula düşer; düşmeyince metin resmî genelgeye döner.
- **Önce:** "Bu yöntem etkilidir. Uygulaması kolaydır. Maliyeti düşüktür."
- **Sonra:** "Yöntem işe yarıyor, uygulaması kolay, maliyeti düşük."

### 24. Retorik soru + hazır cevap bloğu
- **Yüzey:** "Peki bu neden önemli? Çünkü …" / "Peki çözüm ne? …" — başlık gibi kullanılan soru-cevap.
- **Neden YZ:** İngilizce blog şablonu; soru süs, cevap zaten biliniyor. İnsan soruyu gerçekten sorar ya da cevabı vermeden bırakır.
- **Önce:** "Peki bu neden önemli? Çünkü veri, kararın yakıtıdır."
- **Sonra:** "Kaç kişi bunu denedi? Ben denedim, olmadı."

### 25. Sahne kurma: "İşte burada … devreye giriyor / Şöyle düşünün / Hayal edin"
- **Yüzey:** ikinci tekil şahısla hayal kurdurma; ardından benzetme.
- **Neden YZ:** "Here's where X comes in / Imagine ..." — sunum dili. Türkçe yazıda bu ton reklam kokar.
- **Önce:** "İşte burada yapay zekâ devreye giriyor. Şöyle düşünün: bir asistanınız var…"
- **Sonra:** "Yapay zekâ burada işe yarıyor. Asistan gibi düşün."

### 26. Kaynaksız otorite
- **Yüzey:** "uzmanlara göre", "araştırmalar gösteriyor", "birçok kaynak", "bilimsel olarak kanıtlanmış".
- **Neden YZ:** Atıf taklidi; künye yok, doğrulanamaz. Türkçe YZ metinlerinde en güçlü tek işaret sayılıyor ([Düzelti](https://duzelti.com/blog/yapay-zeka-ile-yazildigi-nasil-anlasilir)).
- **Önce:** "Uzmanlara göre bu yöntem en etkili yöntemlerden biridir."
- **Sonra:** "Denedim, işe yaradı. Taner Hoca da aynısını söylüyor."

---

## Bölüm 3 — Biçim işaretleri

### 27. Kalın etiketli madde listeleri
- **Yüzey:** `**Önemli:**`, `**Adım 1:**`, `**Not:**`; her madde kalın etiket + iki nokta.
- **Neden YZ:** Modelin varsayılan çıktı biçimi. Düz yazıda bilgi akışı kesilir; Türkçe okur bunu sunum slaytı gibi okur.
- **Önce:** "**Önemli:** Yedek almayı unutmayın."
- **Sonra:** "Yedek alın. Sonra ağlamayın."

### 28. Emoji başlıklar ve emoji madde işaretleri
- **Yüzey:** `## 🚀 Başlarken`, `✅`, `💡`.
- **Neden YZ:** Pazarlama şablonu; teknik yazıda ve gündelik yazıda yok. Türk forum/Reddit yazısında emoji nadir, varsa ironik.
- **Önce:** "## 🚀 Başlarken"
- **Sonra:** "## Başlarken"

### 29. Eşit paragraflar, aynı ritim
- **Yüzey:** her paragraf 3 cümle, hepsi aynı uzunlukta; metin ızgara gibi.
- **Neden YZ:** Model uzunluk dağılımını düzler. İnsan ritmi bozar: bir uzun cümle, sonra iki kelime.
- **Önce:** "Dijital pazarlama hedef kitleye ulaşmayı sağlar. Doğru stratejiyle bilinirlik artar. Bu da satışları olumlu etkiler."
- **Sonra:** "Reklam verdik. Satış arttı. Bu kadar."

### 30. Kapanış nezaketi
- **Yüzey:** "Umarım yardımcı olmuştur.", "Başka bir sorunuz olursa çekinmeden sorabilirsiniz.", "İyi çalışmalar dilerim."
- **Neden YZ:** Chatbot kapanışı. Türkçe yazışmada "kolay gelsin" var ama bu kalıp çeviri kokar.
- **Önce:** "Umarım bu bilgiler yardımcı olmuştur. Başka bir sorunuz olursa çekinmeden sorabilirsiniz."
- **Sonra:** "Takıldığın yer olursa yaz."

### 31. Söylenmişi özetleyen "Özetle" bloğu
- **Yüzey:** metnin sonunda madde madde tekrar; üstüne "Özetle" başlığı.
- **Neden YZ:** Token üretme alışkanlığı. Web Türkçesinde özet ancak metin uzunsa ve yeni bilgi katıyorsa var.
- **Önce:** "Özetle: dijitalleşme önemlidir, veri kritiktir, uyum şarttır."
- **Sonra:** (özet bloğu silinir; son cümle kapanış olur.)

---

## Bölüm 4 — İnsan yazımından taklit edilecek alışkanlıklar

1. **Devrik cümle ve eksiltili cümle.** "Gelmiyor işte.", "Ben de.", "Yok artık." Yüklem ortada/sonda değil; anlam boşlukta tamamlanır.
2. **Parçacık ve dolgu:** `yani, işte, hani, bir de, şey, açıkçası, vallahi, hadi`. Yazıda ölçülü kullanılır; sohbette yoğun. Bunlar YZ'de neredeyse hiç yok — en kolay insan sinyali.
3. **Deyim ve atasözü.** "Ağzı yanan yoğurdu üfleyerek yer." YZ deyimi bilir ama yanlış bağlamda, açıklayarak kullanır ("yani … demek istiyorum").
4. **Rivayet ve aktarım.** `-mış` ile duyulan: "Adam gitmiş, bakmış, yok." YZ `-dı`ya düzler, rivayet tonu kaybolur.
5. **Kısa, yüklem-sonlu vuruş cümlesi.** "Bitti.", "Olmadı.", "Boşver." Paragrafın ortasında tek kelimelik cümle.
6. **Retorik soru, cevapsız.** "Şimdi ben bunu niye yapayım?"
7. **Ani ara söz.** "Açıkçası", "ha bir de", parantez içi itiraf: "(evet, denedim)".
8. **Konuşma çekimi (register uyarısı).** `napıcaz`, `geliyo`, `yapçam` yalnızca çok gündelik metinde; blogda "ne yapacağız" beklenir. Yanlış register'da kullanınca YZ taklidi gibi durur.
9. **Forum/Reddit/Ekşi Sözlük tonu.** Küçük harfle başlama, noktalama ihmali, cümle ortasında ton değişimi, `abi/kanka/ya/ki` , alıntıya doğrudan cevap. Ekşi'de tanım üslubu ("şu şu olan şey"), Reddit'te tartışma üslubu ("kaynak var mı?"). YZ ikisini de "makale"ye çevirir — en büyük ton kaybı burada.
10. **Somut ayrıntı.** Marka adı, tarih, fiyat, "iki gün önce", "bizim orada". YZ genel kalır.

---

## Bölüm 5 — Register taksonomisi

| Register | `-mektedir` | `siz` | `-dir` | Bağlaç yoğunluğu | Madde/başlık | Em dash | Deyim/argo | Not |
|---|---|---|---|---|---|---|---|---|
| **Resmî/kurumsal** | Meşru | Meşru | Meşru | Orta | Meşru | Az | Hayır | Buradaki YZ riski: şişirilmiş yüklem (#5) ve boş kalıp (#12). |
| **Akademik** | Meşru | Meşru ("biz" tercih) | Meşru | Yüksek, işlevli | Meşru | Az | Hayır | Uzun cümle (#19) meşru; ama #26 kaynaksız otorite asla. |
| **Blog/editöryel** | **Hata** | `sen` tercih | Düşer | Düşük | Az, tercihen düz yazı | Az | Evet | YZ burada en çok yakalanır: #1–#4, #27, #28, #30. |
| **Gündelik/sosyal medya** | **Hata** | `sen` | Düşer | Çok düşük | Yok | Yok | Yoğun | Devrik cümle, parçacık, eksilti zorunlu (#18, Bölüm 4). |
| **Teknik dokümantasyon** | Kısmen (kural/şart) | `siz` veya emir | Düşer | Düşük | Meşru, işlevsel | Az | Hayır | #27 burada meşru; #9, #12, #25 değil. Emir kipi en doğal ton. |

**Kural yazarken:** bir işaret "YZ" diye işaretlenmeden önce register kontrolü yapılmalı. `-mektedir` kurumsal metinde kusur değil; `adeta` edebî metinde kusur değil. Sinyal **register ile uyumsuzluk** ve **yoğunluk**tur, tek başına sözcük değil.

---

## Kaynaklar

- [Devrik cümle — Vikipedi](https://tr.wikipedia.org/wiki/Devrik_c%C3%BCmle) (devrik cümlenin işlevi, "bozuk değil")
- [Büyük ünlü uyumu — Vikipedi](https://tr.wikipedia.org/wiki/B%C3%BCy%C3%BCk_%C3%BCnl%C3%BC_uyumu)
- [Tamlama — Vikipedi](https://tr.wikipedia.org/wiki/Tamlama)
- [Türkçe — Vikipedi](https://tr.wikipedia.org/wiki/T%C3%BCrk%C3%A7e) (eklemeli dil, Oğuz grubu)
- [Düzelti — Bir Metnin Yapay Zekâ ile Yazıldığı Nasıl Anlaşılır?](https://duzelti.com/blog/yapay-zeka-ile-yazildigi-nasil-anlasilir) (kalıp açılış/kapanış, eşit paragraf, bağlaç düzeni, kalın başlık+madde, uydurma kaynak)
- [Humanaizer — YZ metinlerinin ortak özellikleri](https://humanaizer.io/tr/blog/bir-metnin-yapay-zeka-ile-yazildigi-nasil-anlasilir-ipuclari-ve-detaylar) (geçiş ifadesi fazlalığı, duygusal dokunuş eksikliği)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (yapısal işaretlerin İngilizce taban çizgisi: "not X but Y", üçleme, kalın etiket, em dash)
- Ekşi Sözlük `chatgpt` başlığı — gündelik Türkçe yazım örneği olarak: <https://eksisozluk.com/chatgpt--7485348>
