# Katkıda Bulunma Rehberi

Pardus Yol Arkadaşı projesine katkıda bulunmak istediğiniz için teşekkür ederiz! 🎉

## Nasıl Katkıda Bulunabilirsiniz?

### 1. Hata Bildirimi

Bir hata bulduysanız:
- GitHub Issues sayfasında yeni bir issue açın
- Hatayı detaylı açıklayın
- Hatayı yeniden oluşturma adımlarını ekleyin
- Sistem bilgilerinizi paylaşın (Pardus versiyonu, Python versiyonu vb.)

### 2. Özellik Önerisi

Yeni bir özellik önerisi için:
- GitHub Issues sayfasında "Feature Request" etiketi ile issue açın
- Özelliği detaylı açıklayın
- Kullanım senaryolarını belirtin
- Mümkünse mockup veya örnek ekleyin

### 3. Kod Katkısı

Kod katkısında bulunmak için:

1. **Depoyu Fork Edin**
   ```bash
   git clone https://github.com/OttomanTechs/pardus-yol-arkadasi.git
   cd pardus-yol-arkadasi
   ```

2. **Yeni Bir Branch Oluşturun**
   ```bash
   git checkout -b feature/yeni-ozellik
   ```

3. **Değişikliklerinizi Yapın**
   - Kod standartlarına uyun
   - Türkçe yorum satırları ekleyin
   - Anlaşılır commit mesajları yazın

4. **Test Edin**
   ```bash
   python3 src/main.py --debug
   ```

5. **Commit ve Push**
   ```bash
   git add .
   git commit -m "Yeni özellik: Açıklama"
   git push origin feature/yeni-ozellik
   ```

6. **Pull Request Oluşturun**
   - GitHub'da Pull Request açın
   - Değişikliklerinizi detaylı açıklayın
   - İlgili issue'ları referans gösterin

## Kod Standartları

### Python Kod Stili

- **PEP 8** standartlarına uyun
- **Türkçe yorum satırları** kullanın
- **Docstring'ler** Türkçe olmalı
- **Değişken isimleri** İngilizce, açıklayıcı olmalı

Örnek:
```python
def calculate_progress(current_step, total_steps):
    """
    Rehber ilerleme yüzdesini hesapla
    
    Args:
        current_step (int): Mevcut adım numarası
        total_steps (int): Toplam adım sayısı
    
    Returns:
        float: İlerleme yüzdesi (0-100)
    """
    if total_steps == 0:
        return 100.0
    return (current_step / total_steps) * 100
```

### Commit Mesajları

Commit mesajları Türkçe ve açıklayıcı olmalı:

```
✅ İyi örnekler:
- "Spotlight animasyon hızı ayarı eklendi"
- "Dosya işlemleri rehberi güncellendi"
- "Ses yöneticisi hata düzeltmesi"

❌ Kötü örnekler:
- "fix"
- "update"
- "changes"
```

### Yeni Rehber Ekleme

Yeni bir rehber modülü eklemek için:

1. `src/data/tutorials/` dizinine JSON dosyası ekleyin
2. Dosya adı formatı: `XX-rehber-adi.json`
3. JSON şemasına uyun:

```json
{
  "id": "unique-id",
  "title": "Rehber Başlığı",
  "description": "Kısa açıklama",
  "category": "basics|applications|settings|advanced",
  "difficulty": "beginner|intermediate|advanced",
  "estimated_time": 5,
  "icon": "icon-name",
  "prerequisites": [],
  "steps": [
    {
      "title": "Adım Başlığı",
      "description": "Detaylı açıklama",
      "target": "css-selector",
      "target_type": "selector|coordinate|window",
      "duration": 10,
      "animation": "fade|pulse"
    }
  ]
}
```

## Test Etme

Değişikliklerinizi test etmek için:

```bash
# Debug modunda çalıştır
python3 src/main.py --debug

# Belirli bir rehberi test et
python3 src/main.py --tutorial desktop-basics --debug

# Tam ekran modunda test et
python3 src/main.py --fullscreen
```

## Dokümantasyon

- Yeni özellikler için README.md'yi güncelleyin
- Karmaşık fonksiyonlar için docstring ekleyin
- Kullanıcı rehberleri için örnekler verin

## Lisans

Katkılarınız GPL-3.0 lisansı altında yayınlanacaktır.

## İletişim

Sorularınız için:
- **GitHub Issues**: Teknik sorular ve hatalar
- **E-posta**: ottoman.techs@example.com
- **Teknofest**: Yarışma ile ilgili sorular

## Teşekkürler! 🙏

Katkılarınız Pardus ekosistemini güçlendirir ve kullanıcı deneyimini iyileştirir.
