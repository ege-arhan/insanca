# insanca

Türkçe LLM çıktısını, bir Türk'ün yazacağı gibi yeniden yazar. Anlamı korur, uydurmaz.

İngilizce insanlaştırıcıların Türkçede yetersiz kalması üzerine sıfırdan yazıldı. Kural listesi çeviri değil; Türkçe insan metniyle ölçülerek çıkarıldı.

> **Durum:** v0.1. Kurallar ve ölçüm çalışıyor, kullanıcı hakemliğinde test aşamasında.

## Neden Türkçeye ayrı bir araç

`humanizer`, `stop-slop` gibi popüler araçlar cümle düzeyindeki izleri kovalar: em dash, `not X but Y`, `-ing` yan cümleleri, üçlü liste, kalın etiket. Bunların bir kısmı Türkçede karşılıksızdır, asıl izleri ise hiç görmezler.

| İngilizce kural | Türkçede durumu |
|---|---|
| "Em dash'i sil" | Em dash ithal norm. İnsan Türkçesinde **0,98/1000 kelime** var, yani seyrek ama mevcut. Asıl ithal işaret **noktalı virgül köprüsü**. |
| "`not X but Y` yapısını yakala" | `değil` Türkçenin en sık sözcüklerinden; basit arama %90 yanlış pozitif. Yalnız `sadece … değil … aynı zamanda` üçlüsü iz. |
| "Yasak kelime listesi" | Eklemeli dilde kelime listesi tutmaz. İz `-mektedir` yığınında, `gerçekleştirilmektedir` zincirinde, tamlama kulesinde. |
| "Burstiness (cümle uzunluğu varyansı) hedefle" | Türkçede kelime sırası serbest, varyans gürültü. Ölçüt **hece** ve **yüklem konumu**. |
| "Edilgen çatıyı aktife çevir" | Doğru ama eksik: Türkçede `tarafından` + `-ilmektedir` + yardımcı fiil üçlüsü birlikte gelir. |

Türkçede makine kokusunun yarısı **fazlalık**, yarısı **eksiklik**tir: devrik cümle, kısa cümle, parçacık (`yani`, `işte`, `bir de`), somut ayrıntı, tereddüt. İngilizce araçlar yalnız fazlalığı arar; temizledikten sonra metin doğru ama ruhsuz kalır.

## Bu araç neyi farklı yapıyor

1. **Şiddet modeli.** Her kural S1/S2/S3: S1 tek görülmede düzeltilir, S3 yalnız yoğunlukta. "Hepsini düzelt" yaklaşımı yazarın sesini öldürür.
2. **Register kapısı.** `-mektedir` akademik metinde standart, blogda hata. Kural register'a göre açılıp kapanır (`references/register.md`).
3. **Yokluk sinyalleri.** Devrik cümle yokluğu, kısa cümle yokluğu, parçacık yokluğu ayrı iz olarak ölçülür (§29–§34).
4. **Ölçülmüş taban çizgisi.** Kurallar tahmin değil: 175 temiz Türkçe insan kaydı / 21.401 kelime üzerinden çıkarıldı (`data/human-baseline.json`, `scripts/corpus_human.py`).
5. **Çalıştırılabilir kontrol.** `scripts/tells.py` her cümleyi değil metni ölçer, 0–100 skor verir, önce/sonra karşılaştırması yapılabilir.
6. **Aşırı düzeltme kapısı.** %30'dan fazla değişimde dur, %50'de kaynak metne dön.
7. **Reddedilen kurallar.** Denenip elenen 10 kural gerekçesiyle `references/rejected-rules.md` içinde. Bu dosya olmadan araç İngilizce sezgileri Türkçe kural diye satar.

## Hızlı başlangıç

### Skill olarak (Claude Code / Codex)

```bash
git clone https://github.com/ege-arhan/insanca
mkdir -p ~/.claude/skills ~/.dsh/skills
ln -s "$PWD/insanca" ~/.claude/skills/insanca
ln -s "$PWD/insanca" ~/.dsh/skills/insanca
```

Sonra: "şu metni insanca insanlaştır" / "bu Türkçe metin robot gibi duruyor, düzelt".

### CLI olarak

```bash
python3 scripts/tells.py --register blog metin.md          # skor + izler
python3 scripts/tells.py --register akademik tez.md        # register'a göre
echo "metin" | python3 scripts/tells.py -                  # boru hattı
python3 scripts/selftest.py                                # katmanlı doğrulama
```

Bağımlılık yok, yalnız Python 3 standart kütüphanesi.

## Nasıl çalışır

1. **Register belirle** — resmî, akademik, blog, gündelik, teknik.
2. **İzleri işaretle** — S1'ler önce.
3. **Yeniden yaz** — bilgiyi koru, süsü at, cümleyi kur.
4. **Sesi ekle** — devrik cümle, kısa cümle, parçacık, somutluk, tutum. **Sayı/ad/tarih/iddia eklemeden.**
5. **Kontrol et** — `tells.py` skoru düştü mü, değişim %30'u geçti mi, anlam korundu mu.

## Önce / sonra

**Önce (YZ):**
> Uzaktan çalışma, modern iş hayatının ayrılmaz bir parçası haline geldi. Peki bu dönüşüm gerçekten de verimliliğimizi artırıyor mu? Bu soru, dijital çağın en kritik tartışmalarından birini oluşturmaktadır. Bu bağlamda, odak yönetimi bir lüks değil, temel bir beceri haline gelmektedir. Unutulmamalıdır ki, sürdürülebilir bir performans, ancak doğru alışkanlıkların kazanılmasıyla mümkündür. Umarım bu yazı, kendi çalışma düzeninizi yeniden düşünmeniz için bir başlangıç noktası olmuştur.

**Sonra (insanca):**
> Uzaktan çalışma hayatımıza girdiğinden beri aynı soruyu soruyorum kendime: gerçekten daha mı verimliyiz, yoksa sadece ofisin duvarları mı kalktı? Esneklik tarafı kolay. Sabah dokuzda kimse gözümün içine bakmıyor, işimi kendi ritmime göre planlıyorum. Ama ev dediğin yer bir dikkat dağıtma fabrikası. Odak yönetimi artık lüks değil, olmazsa olmaz.

## Ölçüm

Dört registerde dört YZ metni, `insanca` ile yeniden yazıldı, aynı araçla ölçüldü:

| Metin | Önce | Sonra |
|---|---|---|
| Blog / editoryel | 89,9 | 0,0 |
| Kurumsal duyuru | 82,3 | 15,4 |
| Teknik dokümantasyon | 80,8 | 0,0 |
| Sosyal medya | 77,3 | 15,4 |

Skor 0–100. Metinler ve hakem formu `evals/` altında. Kör A/B değerlendirmesi `evals/RUBRIC.md` ile yapılır.

**Sınırlar (dürüstçe):**
- İnsan taban çizgisi sohbet/chat register'ından geliyor; blog metni biraz daha uzun cümle kurar. Devrik oranı ve `-mektedir` sıfırı yine geçerli.
- Noktalı virgül için güvenilir taban çizgisi çıkarılamadı (korpus `;` büyük ölçüde kod parçalarından kirlenmiş).
- Ölçüm YZ tarafı için büyük ve temiz bir "LLM makale Türkçesi" korpusu yok; 4 metinlik referans küçük örneklem.
- Skor, hakemin yerine geçmez. Nihai karar insan okurun.

## Mevcut Türkçe insanlaştırıcılar

Bu proje ilk değil. Türkçe için de araçlar var:

- [bushrabeg/turkce-humanizer](https://github.com/bushrabeg/turkce-humanizer) — 2 faz, 5 register, 5 mutlak yasak
- [genmedya/turkish-native-humanizer](https://github.com/genmedya/turkish-native-humanizer) — 87 K-deseni, eksen modeli, TDK uyumlu
- Birkaç ince fork (`durmazoguzhan/turkish-humanify`, `RizgarOzan/turkce-humanizer` vb.)

Fark: şiddet modeli, ölçülmüş taban çizgisi, çalıştırılabilir skor, reddedilen kurallar dosyası ve yokluk sinyalleri. Kural listesi "sıfırdan" değil, Türkçe korpus ve dilbilgisi üzerinden yazıldı.

## Depo yapısı

```
SKILL.md                    — beceri girişi, iş akışı, S1/S2/S3 özeti
references/patterns-tr.md   — 38 numaralı desen, öncesi/sonrası
references/register.md      — 5 register, ne meşru ne hata
references/rejected-rules.md— elenen kurallar ve gerekçeleri
scripts/tells.py            — 0–100 skor, iz çıkarımı
scripts/corpus_human.py     — insan taban çizgisi çıkarımı
scripts/selftest.py         — katmanlı doğrulama
data/human-baseline.json    — ölçülmüş taban çizgisi
evals/                      — girdiler, çıktılar, hakem formu
research/                   — kaynak taraması (İngilizce + Türkçe)
```

## Yol haritası

- [ ] Blog/editoryel register'ında insan taban çizgisi (şu an sohbet register'ı)
- [ ] Noktalı virgül ve iki nokta için temiz ölçüm
- [ ] Daha büyük kör A/B hakem seti, iki bağımsız hakem
- [ ] Parçacık enjeksiyonunda register-güvenli şablonlar
- [ ] Kelime işlemci eklentisi / API

## Lisans

MIT. Katkı: kural eklemeden önce `references/rejected-rules.md` oku; her yeni desen öncesi/sonrası örneği ve ölçümle gelmeli.
