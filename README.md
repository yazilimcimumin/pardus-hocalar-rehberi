# Pardus Yol Arkadaşı - İnteraktif Kullanıcı Rehberi

![Pardus Logo](https://www.pardus.org.tr/wp-content/uploads/2020/01/pardus-logo.png)

## 📋 Proje Hakkında

**Pardus Yol Arkadaşı**, Windows'tan Pardus'a geçiş yapan öğretmenler ve kullanıcılar için geliştirilmiş interaktif bir on-boarding sistemidir. Özellikle Pardus akıllı tahtalar için optimize edilmiş bu uygulama, kullanıcıların sistemi kolayca öğrenmesini sağlar.

### 🎯 Hedef Kitle
- Pardus akıllı tahta kullanan öğretmenler
- Windows'tan Pardus'a geçiş yapan kullanıcılar
- Pardus'u ilk kez kullanan eğitimciler

### ✨ Özellikler

- **İnteraktif Rehberlik**: Ekrandaki öğelere spotlight efektiyle odaklanma
- **Sesli Anlatım**: Her adım için Türkçe sesli açıklamalar
- **Animasyonlu Gösterim**: Görsel olarak adım adım öğretim
- **Modüler Yapı**: Farklı konular için ayrı rehber modülleri
- **Akıllı Tahta Uyumlu**: Dokunmatik ekran ve büyük ekranlar için optimize edilmiş
- **Hafif ve Hızlı**: Sistem kaynaklarını minimal kullanım

### 📚 Rehber Modülleri

1. **Masaüstü Temelleri**
   - Masaüstüne kısayol ekleme
   - Dosya yöneticisi kullanımı
   - Panel ve menü kullanımı

2. **Dosya İşlemleri**
   - Dosya ve klasör oluşturma
   - Kopyalama, taşıma, silme
   - USB bellek kullanımı

3. **Uygulama Yönetimi**
   - Uygulama başlatma
   - Yazılım merkezi kullanımı
   - Sık kullanılan uygulamalar

4. **Sistem Ayarları**
   - Ekran ayarları
   - Ses ayarları
   - Ağ bağlantısı

5. **Akıllı Tahta Özellikleri**
   - Dokunmatik ekran kullanımı
   - Çoklu dokunuş hareketleri
   - Ekran paylaşımı

## 🛠️ Teknolojiler

- **Python 3.10+**: Ana programlama dili
- **PyQt5**: Grafik arayüz kütüphanesi
- **QtMultimedia**: Ses ve animasyon desteği
- **Debian Packaging**: .deb paket oluşturma

## 📦 Kurulum

### Sistem Gereksinimleri

- **İşletim Sistemi**: Pardus 21 veya üzeri
- **Python**: 3.10+
- **PyQt5**: 5.15+
- **Disk Alanı**: 100 MB boş alan

### Yöntem 1: Debian Paketi ile Kurulum (Önerilen)

```bash
# Paketi kurun
sudo dpkg -i pardus-yol-arkadasi_1.0.0_all.deb

# Bağımlılıkları yükleyin
sudo apt-get install -f
```

### Yöntem 2: Basit Kurulum Scripti

```bash
# Kurulum
sudo bash install.sh

# Kaldırma
sudo bash uninstall.sh
```

### Yöntem 3: Kaynak Koddan Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/OttomanTechs/pardus-yol-arkadasi.git
cd pardus-yol-arkadasi

# Bağımlılıkları yükleyin
sudo apt-get install python3 python3-pyqt5 python3-pyqt5.qtmultimedia

# Uygulamayı çalıştırın
python3 src/main.py
```

## 🚀 Kullanım

### Masaüstünden Başlatma

Uygulama kurulduktan sonra masaüstünde **Pardus Yol Arkadaşı** ikonu görünecektir. İkona çift tıklayarak uygulamayı başlatabilirsiniz.

### Komut Satırından Başlatma

```bash
pardus-yol-arkadasi
```

### İlk Açılışta Otomatik Başlatma

Uygulama ilk kurulumda otomatik olarak başlatılır. Bu özelliği devre dışı bırakmak için:

```bash
# Otomatik başlatmayı kapat
rm ~/.config/autostart/pardus-yol-arkadasi.desktop
```

## 🏗️ Proje Yapısı

```
pardus-yol-arkadasi/
├── src/
│   ├── main.py                 # Ana uygulama giriş noktası
│   ├── ui/
│   │   ├── main_window.py      # Ana pencere arayüzü
│   │   ├── spotlight.py        # Spotlight efekt widget'ı
│   │   └── tutorial_widget.py  # Rehber gösterim widget'ı
│   ├── core/
│   │   ├── tutorial_manager.py # Rehber yönetim sistemi
│   │   ├── audio_manager.py    # Ses yönetim sistemi
│   │   └── config.py           # Yapılandırma yönetimi
│   └── data/
│       ├── tutorials/          # Rehber JSON dosyaları
│       └── audio/              # Ses dosyaları
├── resources/
│   ├── icons/                  # Uygulama ikonları
│   ├── images/                 # Görseller
│   └── styles/                 # QSS stil dosyaları
├── debian/                     # Debian paket yapılandırması
├── docs/                       # Dokümantasyon
├── tests/                      # Test dosyaları
├── requirements.txt            # Python bağımlılıkları
├── setup.py                    # Kurulum scripti
└── README.md                   # Bu dosya
```

## 🔧 Geliştirme

### Geliştirme Ortamı Kurulumu

```bash
# Sanal ortam oluşturun
python3 -m venv venv
source venv/bin/activate

# Geliştirme bağımlılıklarını yükleyin
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Uygulamayı geliştirme modunda çalıştırın
python3 src/main.py --debug
```

### Yeni Rehber Ekleme

Yeni bir rehber modülü eklemek için `src/data/tutorials/` dizinine JSON formatında dosya ekleyin:

```json
{
  "id": "yeni-rehber",
  "title": "Yeni Rehber Başlığı",
  "description": "Rehber açıklaması",
  "steps": [
    {
      "title": "Adım 1",
      "description": "Adım açıklaması",
      "target": "css-selector",
      "audio": "audio/yeni-rehber-1.mp3"
    }
  ]
}
```

### Debian Paketi Oluşturma

```bash
# Paketi oluşturun
dpkg-buildpackage -us -uc -b

# Paket üst dizinde oluşturulacaktır
ls ../*.deb
```

## 🧪 Test

```bash
# Tüm testleri çalıştırın
python3 -m pytest tests/

# Belirli bir test dosyasını çalıştırın
python3 -m pytest tests/test_tutorial_manager.py

# Kod kapsamı raporu
python3 -m pytest --cov=src tests/
```

## 👥 Geliştirici Ekibi

**Ottoman Techs** - Teknofest 2026 Pardus Yarışması

- Proje Yöneticisi: [İsim]
- Yazılım Geliştirici: [İsim]
- UI/UX Tasarımcı: [İsim]
- Test Uzmanı: [İsim]

## 📄 Lisans

Bu proje GPL-3.0 lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen katkıda bulunmadan önce [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📞 İletişim

- **Proje Web Sitesi**: https://github.com/OttomanTechs/pardus-yol-arkadasi
- **E-posta**: ottoman.techs@example.com
- **Teknofest**: https://www.teknofest.org

## 🙏 Teşekkürler

- TÜBİTAK BİLGEM - Pardus geliştirme ekibine
- Pardus topluluğuna
- Teknofest organizasyon komitesine
- Tüm katkıda bulunanlara

---

**Not**: Bu proje Teknofest 2026 Pardus Yarışması için geliştirilmiştir.
