# Pardus Yol Arkadaşı - Proje Yapısı

## 📁 Dizin Yapısı

```
pardus-yol-arkadasi/
│
├── 📄 README.md                    # Ana proje açıklaması
├── 📄 LICENSE                      # GPL-3.0 lisansı
├── 📄 CONTRIBUTING.md              # Katkıda bulunma rehberi
├── 📄 TEKNOFEST_OZET.md           # Teknofest proje özeti
├── 📄 PROJE_YAPISI.md             # Bu dosya
├── 📄 requirements.txt             # Python bağımlılıkları
├── 📄 setup.py                     # Kurulum scripti
├── 🔧 .gitignore                   # Git ignore kuralları
│
├── 🚀 build-deb.sh                 # Debian paketi oluşturma scripti
├── 🚀 run-dev.sh                   # Geliştirme modu çalıştırma
│
├── 📂 src/                         # Kaynak kod
│   ├── 📄 __init__.py
│   ├── 🐍 main.py                  # Ana uygulama giriş noktası
│   │
│   ├── 📂 ui/                      # Kullanıcı arayüzü
│   │   ├── 📄 __init__.py
│   │   ├── 🐍 main_window.py       # Ana pencere (Apple-inspired UI)
│   │   ├── 🐍 spotlight.py         # Spotlight efekt widget'ı
│   │   └── 🐍 tutorial_widget.py   # Rehber gösterim widget'ı
│   │
│   ├── 📂 core/                    # Temel sistem bileşenleri
│   │   ├── 📄 __init__.py
│   │   ├── 🐍 config.py            # Yapılandırma yönetimi
│   │   ├── 🐍 tutorial_manager.py  # Rehber yönetim sistemi
│   │   └── 🐍 audio_manager.py     # Ses yönetim sistemi
│   │
│   └── 📂 data/                    # Veri dosyaları
│       ├── 📂 tutorials/           # Rehber JSON dosyaları
│       │   ├── 📋 01-desktop-basics.json        # Masaüstü temelleri (13 adım)
│       │   ├── 📋 02-file-operations.json       # Dosya işlemleri (15 adım)
│       │   ├── 📋 03-applications.json          # Uygulama yönetimi (7 adım)
│       │   ├── 📋 04-system-settings.json       # Sistem ayarları (8 adım)
│       │   ├── 📋 05-smart-board.json           # Akıllı tahta (15 adım)
│       │   ├── 📋 06-office-applications.json   # Ofis uygulamaları (14 adım)
│       │   ├── 📋 07-internet-email.json        # İnternet ve e-posta (13 adım)
│       │   ├── 📋 08-multimedia.json            # Multimedya (14 adım)
│       │   └── 📋 09-system-maintenance.json    # Sistem bakımı (13 adım)
│       │
│       └── 📂 audio/               # Ses dosyaları (gelecekte)
│
├── 📂 resources/                   # Kaynaklar
│   ├── 📂 icons/                   # Uygulama ikonları
│   │   ├── 📄 README.md
│   │   └── 🔧 create_icon.sh       # İkon oluşturma scripti
│   │
│   ├── 📂 images/                  # Görseller
│   └── 📂 styles/                  # QSS stil dosyaları
│       └── 🎨 main.qss             # Ana stil (Apple-inspired)
│
├── 📂 debian/                      # Debian paket yapılandırması
│   ├── 📄 control                  # Paket kontrol dosyası
│   ├── 📄 rules                    # Paket oluşturma kuralları
│   ├── 📄 changelog                # Değişiklik günlüğü
│   ├── 📄 compat                   # Uyumluluk seviyesi
│   ├── 📄 install                  # Kurulum dosyaları
│   ├── 🔧 postinst                 # Kurulum sonrası script
│   ├── 🔧 prerm                    # Kaldırma öncesi script
│   ├── 📄 pardus-yol-arkadasi.desktop              # Masaüstü dosyası
│   └── 📄 pardus-yol-arkadasi-autostart.desktop    # Otomatik başlatma
│
├── 📂 docs/                        # Dokümantasyon
│   ├── 📄 INSTALLATION.md          # Kurulum rehberi
│   └── 📄 QUICKSTART.md            # Hızlı başlangıç
│
└── 📂 tests/                       # Test dosyaları
    └── 🧪 test_tutorial_manager.py # Rehber yöneticisi testleri
```

## 📊 Proje İstatistikleri

### Kod İstatistikleri
- **Python Dosyaları**: 10 adet
- **Toplam Python Satırı**: ~2,200 satır
- **Rehber Dosyaları**: 9 adet (JSON)
- **Toplam Rehber Adımı**: 112 adım
- **Toplam Rehber İçeriği**: ~108 KB

### Rehber Detayları

| Rehber | Adım Sayısı | Tahmini Süre | Zorluk |
|--------|-------------|--------------|--------|
| Masaüstü Temelleri | 13 | 15 dk | Başlangıç |
| Dosya İşlemleri | 15 | 20 dk | Başlangıç |
| Uygulama Yönetimi | 7 | 8 dk | Başlangıç |
| Sistem Ayarları | 8 | 10 dk | Orta |
| Akıllı Tahta | 15 | 30 dk | Orta |
| Ofis Uygulamaları | 14 | 25 dk | Orta |
| İnternet ve E-posta | 13 | 20 dk | Başlangıç |
| Multimedya | 14 | 18 dk | Başlangıç |
| Sistem Bakımı | 13 | 22 dk | Orta |
| **TOPLAM** | **112** | **~3 saat** | - |

## 🏗️ Mimari Tasarım

### Katmanlı Mimari

```
┌─────────────────────────────────────┐
│     Kullanıcı Arayüzü (UI)         │
│  - MainWindow (Ana Pencere)         │
│  - SpotlightWidget (Vurgulama)      │
│  - TutorialWidget (Rehber)          │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│      İş Mantığı (Core)              │
│  - TutorialManager (Rehber Yönetimi)│
│  - AudioManager (Ses Yönetimi)      │
│  - Config (Yapılandırma)            │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│        Veri Katmanı (Data)          │
│  - JSON Rehber Dosyaları            │
│  - Ses Dosyaları                    │
│  - Yapılandırma Dosyaları           │
└─────────────────────────────────────┘
```

### Veri Akışı

```
Kullanıcı
   ↓
MainWindow (Rehber Seçimi)
   ↓
TutorialManager (Rehber Yükleme)
   ↓
JSON Dosyası (Rehber Verisi)
   ↓
TutorialWidget (Adım Gösterimi)
   ↓
SpotlightWidget (Vurgulama)
   ↓
AudioManager (Ses Oynatma)
```

## 🎨 Tasarım Kararları

### UI/UX Tasarımı
- **Apple-inspired Modern Tasarım**: Minimalist, temiz, profesyonel
- **Yumuşak Renkler**: Göz yormayan, uzun kullanım için uygun
- **Okunabilir Tipografi**: 13pt+ font boyutu, yüksek kontrast
- **Dokunmatik Uyumlu**: 44px+ buton boyutu, kolay hedefleme

### Teknoloji Seçimleri
- **Python**: Hızlı geliştirme, kolay bakım
- **PyQt5**: Zengin widget kütüphanesi, platform bağımsız
- **JSON**: İnsan okunabilir, kolay düzenleme
- **Debian Paketi**: Kolay kurulum, bağımlılık yönetimi

### Modüler Yapı
- Her bileşen bağımsız çalışabilir
- Yeni rehberler kolayca eklenebilir
- Test edilebilir kod yapısı
- Genişletilebilir mimari

## 🔧 Geliştirme Araçları

### Gerekli Araçlar
- Python 3.10+
- PyQt5
- Git
- dpkg-dev (paket oluşturma için)

### Önerilen IDE
- Visual Studio Code
- PyCharm
- Vim/Neovim

### Kod Standartları
- PEP 8 (Python stil rehberi)
- Türkçe yorum satırları
- Docstring'ler (fonksiyon açıklamaları)
- Type hints (tip belirteçleri)

## 📦 Paket Yapısı

### Debian Paketi İçeriği
```
/usr/
├── bin/
│   └── pardus-yol-arkadasi         # Çalıştırılabilir script
├── share/
│   ├── applications/
│   │   └── pardus-yol-arkadasi.desktop
│   ├── pixmaps/
│   │   └── pardus-yol-arkadasi.png
│   └── pardus-yol-arkadasi/
│       ├── main.py
│       ├── ui/
│       ├── core/
│       ├── data/
│       └── resources/
└── /etc/
    └── xdg/
        └── autostart/
            └── pardus-yol-arkadasi.desktop
```

## 🚀 Geliştirme Süreci

### 1. Geliştirme Ortamı Kurulumu
```bash
git clone https://github.com/OttomanTechs/pardus-yol-arkadasi.git
cd pardus-yol-arkadasi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Geliştirme Modu
```bash
./run-dev.sh
```

### 3. Test
```bash
python3 -m pytest tests/
```

### 4. Paket Oluşturma
```bash
./build-deb.sh
```

## 📝 Katkıda Bulunma

Detaylı bilgi için [CONTRIBUTING.md](../CONTRIBUTING.md) dosyasına bakınız.

## 📞 İletişim

- **GitHub**: https://github.com/OttomanTechs/pardus-yol-arkadasi
- **E-posta**: ottoman.techs@example.com

---

**Ottoman Techs** - Teknofest 2026 Pardus Yarışması
