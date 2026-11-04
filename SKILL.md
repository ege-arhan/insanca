---
name: insanca
description: Türkçe LLM çıktısını insan yazısına çevirir. Metin yapay zekâ kokuyorsa, "insanlaştır", "Türkçeleştir", "robot gibi duruyor", "bunu ben yazmışım gibi yap" dendiğinde kullan.
---

# insanca — Türkçe insanlaştırma

Türkçe metni, bir Türk'ün yazacağı gibi yeniden yaz. Anlattığını koru, hiçbir şey uydurma.

## Neden Türkçeye ayrı bir araç gerekti

İngilizce insanlaştırıcıların çoğu cümle düzeyindeki izleri kovalıyor: em dash, üçlü liste, "not X but Y". Bunlar Türkçede de var ama Türkçenin asıl makine kokusu **biçimbilim ve kip**te çıkıyor: `-mektedir` yığını, `gerçekleştirilmektedir` gibi edilgen-yardımcı fiil zinciri, isim tamlaması kuleleri, cümle başında "Bu bağlamda / Ayrıca / Sonuç olarak" ritmi. Türkçede artikel yok, kelime sırası serbest, yüklem sonda. Bu yüzden doğal Türkçe çoğu zaman **devrik cümle**, kısa yüklem, bağlaçsız geçiş ve doldurucu sözcükle ("yani", "işte", "bir de") nefes alır. LLM bunların hiçbirini yapmaz; ders kitabı Türkçesi yazar.

İki sonuç:
1. Kelime listesi kovalamak yetmez. Önce **kip, çatı, isimleşme** düzeltilir.
2. Metin doğru ama "kimse yazmamış" durumdaysa yapılacak son iş ses eklemektir; onu da uydurmadan, yazarın kendi tutumunu tahmin ederek yap.

## Nasıl çalışılır

1. **Register'i belirle.** Aynı kalıp bir yerde kusur, başka yerde standarttır. Beş register: resmî/kurumsal, akademik, blog/editoryel, gündelik/sosyal, teknik dokümantasyon. `references/register.md`.
2. **İzleri işaretle.** En güçlüden başla: §1–§5 tek görülmede düzeltilir; *tek başına zayıf* etiketli olanlar aynı metinde başka izlerle beraber gelmedikçe dokunulmaz.
3. **Yeniden yaz.** Her destekli iddiayı koru. Sıkıcı yeri kısaltabilir, paragrafı bölebilir, sırayı değiştirebilirsin. Kaynakta olmayan sayı, ad, tarih, alıntı, kaynak ekleme. Detay eksikse sor ya da daha sade cümle yaz.
4. **Kontrol.** Sesli oku. "Bunu hangi insan yazdı?" diye sor. Sonra en sık hayatta kalan izleri tekrar ara: §2 cümle başı bağlaçları, §1 kip, §6 isimleşme, §8 üçleme.
5. **Teslim.** Varsayılan: taslak + kalan izlerin listesi + final metin. Dosya verilmişse yalnız final metni yaz; kod bloğu, komut, yol, YAML, veri, bağlantı adresleri değişmez.

Yazar örneği verilmişse örnek her kuralın üstündedir: cümle uzunluğu, kelime seçimi, tırnak ve noktalama alışkanlığı örnekten kopyalanır.

## İzler — en güçlüden

Ayrıntı, öncesi/sonrası örnek, Türkçe yüzey işaretleri: `references/patterns-tr.md`.

### A. Kip ve çatı (Türkçenin asıl imzası)

**§1 `-mektedir/-maktadır` yığını.** Gündelik ve blog metninde `-yor`/geniş zaman kullanılır. `-mektedir` akademik ve resmî metinde meşrudur, ama bir blog yazısında her cümlede görünüyorsa makine yazmıştır. *Tek başına orta, üç kez geçerse güçlü.*

**§2 Edilgen + yardımcı fiil zinciri.** `gerçekleştirilmektedir`, `sağlanmaktadır`, `sunulmaktadır`, `hedeflenmektedir`, `öngörülmektedir`. Faili saklar. Türkçe insan yazısı çoğu zaman faili söyler: "ekip yapıyor", "sistem yapıyor", "ben yaptım". Aktif çatıya çevir; aktörü bilmiyorsan "yapılıyor" gibi sade edilgen bırak, `-ilmektedir`i kes.

**§3 Yardımcı fiil şişmesi.** `gerçekleştirmek`, `sağlamak`, `sunmak`, `oluşturmak`, `taşımak`, `icra etmek` → yerine `yapmak`, `vermek`, `olmak`, `etmek`, `çıkarmak`. "Toplantı gerçekleştirildi" → "toplantı yapıldı" ya da "toplandık".

**§4 İsim tamlaması kulesi ve mastar yığını.** Üç ve daha fazla `-in -si` zinciri, `-mek/-mak` ile kurulmuş üçlü mastar ("analiz etmek, değerlendirmek ve optimize etmek için") Türkçeyi boğar. Fiilleştir, böl.

### B. Cümle başı kalıpları (en kolay yakalanan)

**§5 Bağlaç tiki.** Paragrafların çoğu `Ayrıca / Bununla birlikte / Buna ek olarak / Dolayısıyla / Böylece / Bu nedenle / Bu bağlamda / Bu doğrultuda / Sonuç olarak / Özetle / Kısacası` ile başlıyorsa metin makine. İnsan Türkçesi çoğu paragrafa **bağlaçsız** başlar; ilişki zaten içerikten anlaşılır. Fazlalıkları sil, bir iki tanesini bırak.

**§6 "Peki ...?" açılışı ve sahne kurma.** `Peki bu ne anlama geliyor?`, `Şöyle düşünün`, `Hayal edin`, `Hadi birlikte bakalım`, `İşte burada X devreye giriyor`, `Gelin ... inceleyelim`. Noktayı söylemek yerine noktaya yürüyor. Girişi sil, cümleyi kur.

**§7 Karşı çıkılmayan itiraz.** `Bu, X'in önemsiz olduğu anlamına gelmez`, `Yanlış anlaşılmasın`, `Şunu belirtmek gerekir ki`, `Kuşkusuz`, `Elbette`. Kimsenin yapmadığı itirazı savunmak. Sil; gerçek bir iddia taşıyorsa iddiayı yaz.

### C. Şişirme ve klişe

**§8 Anlam şişirme.** `büyük önem taşımaktadır`, `kritik bir rol oynamaktadır`, `hayati önem arz etmektedir`, `temelini oluşturmaktadır`, `zengin bir ... sunmaktadır`, `sayısız fırsat`, `kilit faktör`, `vazgeçilmez bir unsur`. Sıradan bilgiyi tarihi olay gibi sunar. Bilgiyi koru, süsü at.

**§9 Derin söyleyiş.** `aslında mesele şu ki`, `işin özü`, `gerçek soru şu`, `temelde`, `esasen`, `bir anlamda`, `adeta`, `sanki`. Boş aforizma. Yerine somut iddia.

**§10 Satış dili.** `zengin kültürel miras`, `büyüleyici güzellik`, `eşsiz deneyim`, `kusursuz`, `yenilikçi ve sürdürülebilir`, `göz alıcı`, `ideal çözüm`. Ne olduğunu söyle.

**§11 Üçleme zorlaması.** `hız, güvenlik ve kullanılabilirlik` gibi üçlü listeler, üç paralel örnek, üç sıfat. Anlam üç istemiyorsa böl. Madde listesi yerine nesir daha doğal.

**§12 `sadece ... değil, aynı zamanda ...`.** Negatif yarısı kimsenin iddia etmediği bir şeyi çürütür. Doğrudan söyle. Aynı işi gören: `X değil, Y`, `-den çok`, iki cümleye bölünmüş hali ("Bu X demek değildir. Bu Y demektir.").

### D. Biçim ve dolgu

**§13 Em dash.** Türkçe insan yazısı `—` yerine virgül, iki nokta, parantez ya da nokta kullanır. Yazarın örneğinde varsa oranı koru. Tire (`-`) ve kod içi işaretlere dokunma. *Tek başına zayıf.*

**§14 Bold etiketi ve emoji başlık.** `**Hız:** ...` biçiminde etiketli listeler, emoji ile açılan satırlar, her maddeye kalın kelime. Süsü kaldır, etiket bilgi taşımıyorsa nesre çevir.

**§15 Türkçede olmayan başlık düzeni.** Her kelimesi büyük başlık (`Hızlı Ve Güvenilir Çözümler`) İngilizce title case çevirisidir. Türkçede cümle düzeni kullanılır.

**§16 Makale hakkında yazmak.** "Bu yazıda ... ele alınmaktadır", "Aşağıda ... yer almaktadır", "Bu rehber, ... amaçlamaktadır". Okurun gözüyle gördüğünü anlatmayı kes; konuya gir.

**§17 Sohbet artığı.** `Umarım yardımcı olmuştur`, `Başka sorunuz olursa`, `Keyifli okumalar`, `İyi çalışmalar`, `Elbette!`, `Harika soru!`. Sil.

**§18 Belirsiz bağ.** `ile ilişkili`, `bağlantılı olarak`, `konuyla ilgili olarak`, `-e yönelik`. İlişkinin ne olduğunu söyle; söyleyemiyorsan cümleyi at.

**§19 İngilizceden çeviri kokusu.** `-e sahip olmak` ("birçok avantaja sahiptir" → "birçok avantajı var"), `etkili bir şekilde`, `verimli bir şekilde`, `başarılı bir şekilde` zarf şişmesi, her cümlede `-e yönelik`/`konusunda`, "X yapmak önemlidir" → "X yapmak lazım", sıfat yığını.

**§20 Aşırı ölçülülük.** `oldukça`, `son derece`, `bir hayli`, `gayet`, `pek çok açıdan` üst üste. Bir tanesini bırak. *Tek başına zayıf.*

### E. Ses (son adım, uydurmadan)

Doğru ama ruhsuz metin, izler silindikten sonra hâlâ makine gibi durur. Türkçe insan yazısının nefesi:

- **Devrik cümle.** "Bunu ben de düşündüm, söylemedim." Yüklem ortada ya da başta; her cümle fiille bitmez.
- **Kısa cümle.** Uzun cümlenin ardından üç kelimelik cümle gelir. Ritim tek düze değil.
- **Doldurucu.** `yani`, `işte`, `hani`, `bir de`, `tabii`, `açıkçası`, `bence`, `sanırım`, `galiba` — register'e göre, ölçülü.
- **Bağlaçsız geçiş.** Paragraf başında bağlaç yok. İnsan böyle yazar.
- **Somutluk.** "belirli bir süre" değil "üç hafta"; "birçok kişi" değil "bizim ekip".
- **Tereddüt ve tutum.** "Bilemiyorum", "pek emin değilim", "bence yanlış". Blog ve gündelik metinde izin var; teknik ve hukuki metinde yok.
- **Parantez ve kendini düzeltme.** "(yani ...)", "aslında hayır".
- **Rivayet ve aktarım.** `-mış` ile duyum aktarmak Türkçenin doğal aracı; LLM kullanmaz.

Ses eklemek yeni bilgi eklemek değildir: tutum, ritim ve bağlaç seçimi eklenir; sayı, ad, iddia eklenmez.

## Dokunma

Alıntı, özel ad, terim, ticari marka, hukuki/güvenlik uyarısı, sayı, tarih, kaynak atfı, kod, komut, yol, tablo verisi olduğu gibi kalır. `-mektedir` akademik ve resmî metinde kusur değildir. 30 Kasım 2022 öncesi metin AI yazmış olamaz. Tek bir iz tek başına kanıt değildir; izler **küme** halinde anlam kazanır.

## Araç

`python3 scripts/tells.py METIN.md` — iz yoğunluğunu ve metrikleri sayıyla verir. Değişiklik öncesi/sonrası skoru karşılaştırmak için kullan.

## Kaynak

Kalıplar Wikipedia "Signs of AI writing" listesinden, popüler insanlaştırma araçlarının yapısal yaklaşımından ve Türkçe insan/LLM metin korpusunun karşılaştırmalı ölçümünden türetildi. Ayrıntı: `research/`.
