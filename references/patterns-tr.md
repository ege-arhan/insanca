# Türkçe desen kataloğu

Numaralar sabittir, boşluksuzdur. Yeni bir desen ancak mevcut hiçbiri onu kapsamıyorsa numara alır.

**Şiddet ölçeği** (İngilizce araçlardaki "hepsini düzelt" yaklaşımının yerine):

| Kod | Anlam | Davranış |
|---|---|---|
| **S1** | Tek görülmede makine işareti | Bir kez görüldüğünde düzelt |
| **S2** | Doğal olarak 1–2 kez geçer | 3+ görülürse ya da başka izlerle beraberse düzelt |
| **S3** | Yalnız yoğunlukta anlam kazanır | Ritim/yoğunluk ölçümü desteklemiyorsa dokunma |

Ölçülmüş insan taban çizgisi (175 temiz Türkçe sohbet kaydı, 21.401 kelime, `data/human-baseline.json`, `scripts/corpus_human.py`): cümle medyanı **12 kelime**, cümlelerin **%28**'i 8 kelime veya daha kısa, **%3,5**'i 40 kelimeden uzun, yüklem-sonlu cümle oranı **%32–36** (yani cümlelerin çoğu ya devrik ya eksiltili), `-mektedir` **0,00/1000 kelime**, `-yor` 16,8/1000, `-mış` 7,4/1000, em dash 0,98/1000, parantez 1,3/1000, `yani` 1,26/1000. Bu sayılar sohbet register'ına ait; blogda cümle biraz uzar ama `-mektedir` sıfırı ve devrik alışkanlığı değişmez.

---

## A. Kip, çatı, biçimbilim — Türkçenin asıl imzası

### §1 `-mektedir/-maktadır` enflasyonu — **S1** (blog/gündelik), **S3** (akademik/resmî)

**Yüzey:** `...maktadır`, `...mektedir`, `...ilmektedir`, `...ecektir`, `...mıştır` yığını. Çoğu zaman `siz` ile birlikte gelir.
**Neden:** Model eğitim verisindeki resmî Türkçeyi (mevzuat, gazete, tez) varsayılan kip yapar. İnsan sohbet Türkçesinde bu ek **hiç** görünmüyor (ölçüm: 0,00/1000). Blog metninde her 2-3 cümlede bir `-mektedir` varsa metin makinedir.
**Önce:** "Uzaktan çalışma, esnek bir çalışma modeli sunmaktadır. Bu model, çalışanların motivasyonunu artırmaktadır."
**Sonra:** "Uzaktan çalışma esneklik veriyor. Motivasyonu da artırıyor, en azından bende öyle oldu."
**Dokunma:** Akademik makale, resmî yazı, hukuki metin, sözleşme, şartname.

### §2 Edilgen + yardımcı fiil zinciri — **S1**

**Yüzey:** `gerçekleştirilmektedir`, `sağlanmaktadır`, `sunulmaktadır`, `hedeflenmektedir`, `öngörülmektedir`, `yapılması planlanmaktadır`, `-ıl-abil-mektedir`.
**Neden:** Faili saklar, eylemi isme çevirir. Türkçe eklemeli bir dil; zincir uzadıkça `yap-tır-ıl-a-bil-mek` gibi okunmaz birikimler çıkar. İnsan çatıyı sadeleştirir.
**Önce:** "Süreç kapsamında gerekli optimizasyonlar gerçekleştirilerek verimlilik artışı sağlanmıştır."
**Sonra:** "Süreci hızlandırdık, verim de arttı."

### §3 Yardımcı fiil şişmesi — **S2**

**Yüzey:** `gerçekleştirmek`, `sağlamak`, `sunmak`, `oluşturmak`, `taşımak`, `icra etmek`, `vücut bulmak`.
**Neden:** İngilizce `perform/provide/offer/create` fiillerinin birebir karşılığı. Türkçede eylem genelde tek fiille kurulur: `yapmak`, `vermek`, `olmak`, `etmek`, `çıkarmak`, `toplanmak`.
**Önce:** "Toplantı gerçekleştirildi ve kararlar oluşturuldu."
**Sonra:** "Toplandık, kararları aldık." / "Toplantı yapıldı, kararlar çıktı."

### §4 İsim tamlaması kulesi — **S2**
**Yüzey:** üç ve daha fazla `-in/-si` katmanı: "içerik üretim süreçlerinin optimizasyonuna yönelik yaklaşımların geliştirilmesi".
**Neden:** İngilizce isim kümesinin (`content production process optimization approaches`) çevirisi. Türkçede tamlama normaldir, kule değildir.
**Çözüm:** En içteki tamlamayı fiilleştir, kuleyi ikiye böl.

### §5 Mastar yığını — **S2**
**Yüzey:** "analiz etmek, değerlendirmek ve optimize etmek için"; arka arkaya `-mek/-mak`.
**Çözüm:** Eylemlerin bir kısmını çekimli fiile çevir. "Önce analiz ediyorsun, sonra bakıyorsun neyi düzelteceğine."

---

## B. Geçiş ve cümle başı kalıpları

### §6 Geçiş dolgusu — **S1**
**Yüzey:** `Bu bağlamda`, `Bu doğrultuda`, `Bu çerçevede`, `Bu kapsamda`, `Bu noktada`, `Söz konusu`, `Bahse konu`, `İlgili olarak`.
**Neden:** Paragrafı içerik eklemeden bağlar; İngilizce `in this context / in this regard` kalıbının çevirisi.
**Ölçüm:** Metinde iki ve fazla varsa hepsini sil, bir tanesini bile çoğu zaman sil.
**Önce:** "Bu bağlamda, odak yönetimi temel bir beceri haline gelmektedir."
**Sonra:** "Odak yönetimi artık temel beceri."

### §7 Bağlaç rotasyonu — **S1**
**Yüzey:** Paragrafların çoğu `Ayrıca / Bununla birlikte / Buna ek olarak / Öte yandan / Dolayısıyla / Böylece / Bu nedenle / Sonuç olarak / Özetle / Kısacası` ile başlıyor.
**Neden:** Model her paragrafa bir bağlaç takmak zorunda sanır. İnsan Türkçesi paragrafa **bağlaçsız** başlar; ilişki içerikten anlaşılır.
**Çözüm:** Başlangıçların çoğunu sil. Kalanları gerekiyorsa içeri taşı ("Bunu yapmadan önce...").

### §8 Karşı çıkılmayan itiraz — **S1**
**Yüzey:** `Yanlış anlaşılmasın`, `Bu, X'in önemsiz olduğu anlamına gelmez`, `Şunu belirtmek gerekir ki`, `Kuşkusuz`, `Elbette`, `Tabii ki`, `Hiç şüphesiz`.
**Neden:** Önceki taslaktan kalan savunma. Kimsenin yapmadığı itirazı çürütmek.
**Çözüm:** Sil. Gerçek bir iddia taşıyorsa iddiayı doğrudan yaz.

### §9 Didaktik hatırlatma — **S1**
**Yüzey:** `Unutulmamalıdır ki`, `Unutmayın`, `Belirtmek gerekir ki`, `Altını çizmek gerekir`, `Dikkat edilmesi gereken nokta`.
**Neden:** `it should not be forgotten that` — okura ders verme tonu. İnsan ya yazmaz ya parantezde itiraf eder.
**Önce:** "Unutulmamalıdır ki her yatırımın bir riski vardır."
**Sonra:** "Her yatırımda risk var. Kimse söylemiyor ama var."

### §10 Sahne kurma ve retorik soru bloğu — **S1**
**Yüzey:** `Peki bu ne anlama geliyor?`, `Şöyle düşünün`, `Hayal edin`, `Hadi birlikte bakalım`, `Gelin ... inceleyelim`, `İşte burada X devreye giriyor`, `Şimdi ... bakalım`. Ardından hemen cevabı gelir.
**Neden:** Noktayı söylemek yerine noktaya yürür. İnsanın retorik sorusu cevapsız kalır; modelinki iki satır sonra cevaplanır.
**Çözüm:** Girişi sil, cevabı cümle olarak yaz. Retorik soru bırakacaksan cevaplamayı bırak.

---

## C. Şişirme ve klişe

### §11 Anlam şişirme — **S1**
**Yüzey:** `büyük önem taşımaktadır`, `kritik bir rol oynamaktadır`, `hayati önem arz etmektedir`, `temelini oluşturmaktadır`, `vazgeçilmez bir unsurdur`, `kilit faktör`, `kilometre taşı`.
**Neden:** Sıradan bilgiyi tarihi olay gibi sunar; eklediği tek şey ağırlık.
**Önce:** "Güven, her ilişkinin temelini oluşturur."
**Sonra:** "Güven olmadan ilişki yürümez."

### §12 Zenginlik ve potansiyel dili — **S1**
**Yüzey:** `zengin bir ... sunar`, `geniş bir yelpaze`, `sayısız fırsat`, `eşsiz bir deneyim`, `derin bir anlayış`, `potansiyel vaat ediyor`, `ufuk açıcı`.
**Neden:** Ne olduğunu söylemeden övgü. Çeviri kokusu güçlü.
**Çözüm:** Övgüyü at, nesneyi söyle.

### §13 Derin söyleyiş — **S2**
**Yüzey:** `aslında mesele şu ki`, `işin özü`, `gerçek soru şu`, `temelde`, `esasen`, `bir anlamda`, `adeta`, `sanki`, `bir nevi`.
**Neden:** Boş aforizma. `adeta` edebî metinde kusur değil, blogda dolgu.

### §14 `sadece ... değil, aynı zamanda ...` — **S1**
**Yüzey:** `sadece/yalnızca X değil, aynı zamanda Y`, `X değil, Y`, `-den ziyade`, ikiye bölünmüş hali: "Bu X demek değildir. Bu Y demektir."
**Neden:** Negatif yarısı kimsenin iddia etmediği bir şeyi çürütür; pozitif yarı daha büyük görünsün diye var.
**Önce:** "Bu sadece teknik bir iyileştirme değil, aynı zamanda size verdiğimiz değerin yansımasıdır."
**Sonra:** "Açılış hızı düştü, şifreleme her planda açık."

### §15 Zorunlu üçleme — **S2**
**Yüzey:** üç paralel sıfat, üç maddelik liste, üç örnek; "hız, güvenlik ve kullanılabilirlik".
**Neden:** Üç, tamlık hissi verir; anlam üç istemese de gelir. Türkçede üçlü sıfat dizisi edebî değil, sunum dilidir.
**Çözüm:** Maddeleri birleştir; en güçlüyü geliştir; ikiye ya da dörde çevir.

### §16 Kaynaksız otorite — **S1**
**Yüzey:** `uzmanlara göre`, `araştırmalar gösteriyor ki`, `bilim insanları`, `sektör raporları`, `birçok kaynak`, `genel kabul görmüş`.
**Neden:** İsimsiz otorite, iddianın kendisinin zayıf olduğunu gizler. Kaynağı adlandır ya da iddiayı at.

### §17 Satış dili — **S2**
**Yüzey:** `zengin kültürel miras`, `büyüleyici güzellik`, `göz alıcı`, `kusursuz`, `ideal çözüm`, `yenilikçi ve sürdürülebilir`, `mükemmeliyet`.
**Neden:** Metin tanıtım broşürüne döner. Ne olduğunu söyle.

---

## D. Sözdizimi ve çeviri kokusu

### §18 Devrik cümle yokluğu — **S1** (yokluk sinyali)
**Yüzey:** Metindeki her cümle düz SOV, yüklem hep sonda, cümle başı hep özne. Tek devrik, tek eksiltili cümle yok. Ölçüm: insan yazısında yüklem-sonlu cümle oranı **%39**, yani çoğunluk devrik/eksiltili.
**Neden:** Model ders kitabı sırasını tekrarlar; vurgu için sıra oynatmaz. Türkçede sıra değişimi **vurgu** taşır: "Kitabı Ali okudu" ≠ "Ali kitabı okudu".
**Çözüm:** Paragrafta 1–3 cümleyi devrik kur. Yüklem ortaya/başa gelsin. Kısa cümle serpiştir (insan metninin %28'i 8 kelime altı).

### §19 İngilizce calque'i — **S1**
**Yüzey:** `-e sahip olmak` ("birçok avantaja sahiptir" → "birçok avantajı var"), `ihtiyaç duyulmaktadır` → "gerekiyor", `X yapmak önemlidir` → "X yapmak lazım", `-e yönelik`/`konusunda` her cümlede, `etkili bir şekilde`/`verimli bir şekilde`/`başarılı bir şekilde` zarf şişmesi, gereksiz `bir` ("bir çözüm sunar"), `-mek için tasarlanmıştır`.
**Neden:** Yüzeyde Türkçe, iskeleti İngilizce. Çeviri kokusu en çok buradan gelir.
**Çözüm:** Cümleyi İngilizce iskeletinden kurtar: özne + fiil + nesne, zarf yerine fiil.

### §20 Kişi ve kip çatlağı — **S1**
**Yüzey:** `siz` ile `-mektedir` bir arada ama içerik samimi; ya da `sen` ile resmî çekim; `biz` ile tek kişilik deneyim ("ekibimiz olarak ben").
**Neden:** Register uyumsuzluğunun en hızlı teşhisi. Türkçede kibar `siz` + `-mektedir` doğal eştir; `siz` + "kanka" çatlar.
**Çözüm:** Metnin register'ını seç, kişiyi ve kipi ona göre düzle.

### §21 Uzun dönemli cümle + yan cümle yığını — **S2**
**Yüzey:** 40+ kelime, iç içe `-diği`, `-erek`, `-ken`, `-se`, `ki`'li yan cümleler; tek cümlede üç fikir.
**Ölçüm:** İnsan metninin yalnız %3,8'i 40 kelimeden uzun. Blog metni bu oranı aşarsa akademik register'a kaymıştır.
**Çözüm:** Böl. Kısa cümle bırak.

### §22 Belirsiz bağ ve soyutlama — **S2**
**Yüzey:** `ile ilişkili`, `bağlantılı olarak`, `konuyla ilgili olarak`, `X açısından`, `bağlamında`, soyut isim yığını (`süreç`, `yaklaşım`, `perspektif`, `dinamik`, `paradigma`).
**Neden:** İlişkinin ne olduğunu söylemez. İngilizce `associated with / in terms of` çevirisi.
**Çözüm:** İlişkiyi adlandır. Adlandıramıyorsan cümleyi at.

---

## D2. Eklemeli dil tuzakları — İngilizce araçların hiç görmediği katman

Türkçe eklemeli ve ortaç seven bir dil. İngilizceden çevrilen metin sözcüklerde değil **yapıda** çeviri kalır. Bu dört desen, kelime listesiyle yakalanamaz.

### §35 Sola dallanan ortaç zinciri — **S2**
**Yüzey:** `-dığı belirtilen`, `-duğu görülen`, `-eceği öngörülen`, `-diği ifade edilen`, `yapıldığı bilinen`, art arda `-en/-an` ortaçları.
**Neden:** İngilizce sağa dallanan `the fact that ... which ...` yapısının Türkçede sola çevrilmiş hali; cümle açılmadan kapanıyor. İnsan konuşurken ortacı bölüp yeni cümle kurar.
**Önce:** "Yapılan araştırmaların, uzaktan çalışmanın verimliliği artırdığını ortaya koyduğu belirtilmektedir."
**Sonra:** "Araştırmalar uzaktan çalışmanın verimliliği artırdığını söylüyor."

### §36 `tarafından` ile fail — **S2**
**Yüzey:** `... tarafından gerçekleştirilmiştir`, `... tarafından sağlanmaktadır`, `... tarafından yönetilmektedir`.
**Neden:** İngilizce `by` + edilgen. Türkçede fail belliyse edilgen hiç kurulmaz: "ekip yaptı", "sistem yönetiyor". `tarafından` çoğu zaman §2 ve §3 ile birlikte gelir.
**Çözüm:** Aktife çevir; fail gerçekten bilinmiyorsa sade edilgen bırak ("yapıldı"), `tarafından`ı at.

### §37 `bir` şişmesi — **S2**
**Yüzey:** `bir çözüm sunar`, `bir yaklaşım geliştirmek`, `bir süreç olarak`, `bir anlayış`, her soyut ismin önünde `bir`.
**Neden:** Türkçede artikel yok; İngilizce `a/an` çevrilirken her isme `bir` serpilir. Türkçede `bir` gerçekten belirsizlik/sayı bildiriyorsa durur.
**Çözüm:** Anlam taşımayan `bir`leri sil: "kapsamlı bir çözüm sunar" → "kapsamlı çözüm sunuyor".

### §38 Noktalı virgül köprüsü — **S3**
**Yüzey:** iki bağımsız cümleyi `;` ile bağlamak, `;` öncesi/sonrası boşluk, madde içinde `;` ile ayırma.
**Neden:** İngilizcede iki bağımsız cümleyi bağlamanın standart yolu; Türkçede insan ya nokta koyar ya bağlaçla virgül kullanır. Em dash yasağı ithal bir norma dayanır; Türkçede makine kokusu daha çok bu köprüden gelir (blog metninde sayıca göze batıyorsa düzelt; güvenilir Türkçe taban çizgisi bu işaret için çıkarılamadı, ölçüm kod parçalarıyla kirli).
**Çözüm:** Nokta ya da `, çünkü/ama/bu yüzden`. Kod içindeki `;`ye dokunma.

## E. Biçim

### §23 Em dash ve iki nokta süsü — **S3**
**Ölçüm:** İnsan Türkçesinde em dash 0,98/1000 kelime. Yani **yasak değil, seyrek**. `—` ile süslenmiş cümle üç-beş taneyi geçiyorsa düzelt. Yazarın örneğinde varsa oranını koru. Kod ve yol içindeki tireye dokunma. (§38 ile birlikte bak: asıl ithal işaret em dash değil, noktalı virgül köprüsüdür.)
**Çözüm:** Virgül, iki nokta, parantez ya da nokta.

### §24 Kalın etiket ve emoji başlık — **S2** (teknikte meşru)
**Yüzey:** `**Hız:** ...`, `💡 **Önemli:**`, `🚀`, `▼`, `→`, her maddeye kalın kelime, her bölüm arasında `---`.
**Neden:** Dekorasyon her öğeye uygulanmış. Kalın etiket bilgi taşımıyorsa nesre çevir.

### §25 Türkçede olmayan başlık düzeni — **S2**
**Yüzey:** `Hızlı Ve Güvenilir Çözümler` — her kelime büyük. İngilizce title case çevirisi. Türkçede cümle düzeni: `Hızlı ve güvenilir çözümler`.

### §26 Metin hakkında yazmak — **S2**
**Yüzey:** `Bu yazıda ... ele alınmaktadır`, `Aşağıda ... yer almaktadır`, `Bu rehber ... amaçlamaktadır`, `Bu bölümde ... incelenecektir`.
**Çözüm:** Okurun gözüyle gördüğünü anlatmayı kes; konuya gir. Değişiklik günlüğü, sürüm notu ve göç rehberi istisna.

### §27 Sohbet artığı — **S1**
**Yüzey:** `Umarım yardımcı olmuştur`, `Başka sorunuz olursa`, `Keyifli okumalar`, `İyi çalışmalar`, `Elbette!`, `Harika soru!`, `Tabii, işte`, `İşte karşınızda`.
**Çözüm:** Sarıcıyı sil, içeriği tut.

### §28 Belirsizlik bahanesi ve tahmin — **S1**
**Yüzey:** `bilgilerim ... itibariyle`, `sınırlı bilgi mevcut`, `kesin bilgi bulunmamakla birlikte`, `muhtemelen ... olduğu düşünülmektedir`, `olduğu tahmin edilmektedir`.
**Neden:** Model bilgisinin bittiği yeri söyler, sonra boşluğu tahminle doldurur.
**Çözüm:** Neyin kaynakta olmadığını söyle ya da cümleyi at. Tahmini gerçek gibi yazma.

---

## F. Yokluk sinyalleri — çeviri araçlarında olmayan katman

İngilizce insanlaştırıcılar yalnız **fazlalık** arar. Türkçede makine kokusunun yarısı **eksiklik**tir. Aşağıdakiler metinde yoksa, izler temizlenmiş olsa bile metin ruhsuz kalır.

| # | Eksik olan | İnsan metninde beklenen | Nasıl eklenir |
|---|---|---|---|
| **§29** | Devrik/eksiltili cümle | Paragraf başına 1–3 devrik | Yüklemi öne al, art arda kısa cümle |
| **§30** | Parçacık | `yani`, `işte`, `hani`, `bir de`, `açıkçası`, `tabii` — blogda 1–2/1000 kelime | Ölçülü serp; register gündelikse artır |
| **§31** | Somut ayrıntı | sayı, tarih, ad, "iki gün önce", "bizim orada" | **Uydurma yok**: kaynakta varsa öne çıkar, yoksa okura sor |
| **§32** | Tutum ve tereddüt | `bence`, `sanırım`, `bilemiyorum`, `pek emin değilim` | Yalnız görüş/blog register'ında; teknik ve hukukta yok |
| **§33** | Ara söz ve kendini düzeltme | "(yani...)", "aslında hayır" | Eklemek yeni bilgi eklemek değildir, tutum eklemektir |
| **§34** | Ritim çeşitliliği | Kısa cümle oranı %25–35, uzun cümle <%10 | Ardışık aynı uzunlukta cümleleri kır |

**Ölçü notu:** Türkçede ritim kelime-cümle varyansıyla değil **hece sayısı ve yüklem konumuyla** ölçülür. Kelime sırası serbest olduğu için varyans yanıltır; hece uzunluğundaki değişim ve yüklemin sonda/ortada/başta olma dağılımı asıl sinyaldir.

Ses eklerken kural: **tutum, ritim, bağlaç ve kişi eklenir; sayı, ad, tarih, iddia, kaynak eklenmez.**

---

## Aşırı düzeltme kapısı

Her kural birlikte uygulanınca metin yazarın sesinden kopar. Sınırlar (im-not-ai'den uyarlanmış):

- **%30'dan fazla değişim:** dur, hangi değişikliklerin anlam taşıdığını listele, gereksizleri geri al.
- **%50'den fazla değişim:** metni baştan yazmışsın; kaynak metne dön.
- **Kaynak metin zaten iyiyse** ("bu metin insan yazısı gibi duruyor") sonucu döndür ve hiç düzenleme.

Kapsam dışı (hiç dokunulmaz): sayı, birim, tarih, özel ad, alıntı, yasal metin, terim, kod, komut, yol, bağlantı adresi, tablo verisi.

## Reddedilen kurallar

Test edilip **elenen** kurallar `references/rejected-rules.md` dosyasında gerekçesiyle duruyor. Yeni kural eklemeden önce orayı oku: aynı hataya ikinci kez düşmemek için var.
