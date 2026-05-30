# Pardus Yol Arkadaşı - Kurulum Rehberi

## 📋 Sistem Gereksinimleri

### Minimum Gereksinimler
- **İşletim Sistemi**: Pardus 21 veya üzeri
- **İşlemci**: 1 GHz veya daha hızlı
- **RAM**: 2 GB
- **Disk Alanı**: 100 MB boş alan
- **Ekran Çözünürlüğü**: 1024x768 veya üzeri

### Önerilen Gereksinimler
- **İşletim Sistemi**: Pardus 23 (en son sürüm)
- **İşlemci**: 2 GHz çift çekirdekli
- **RAM**: 4 GB veya üzeri
- **Disk Alanı**: 500 MB boş alan
- **Ekran Çözünürlüğü**: 1920x1080 (Full HD)
- **Dokunmatik Ekran**: Akıllı tahta için önerilir

## 📦 Kurulum Yöntemleri

### Yöntem 1: Debian Paketi ile Kurulum (Önerilen)

1. **Paketi İndirin**
   ```bash
   # GitHub'dan en son sürümü indirin
   wget https://github.com/OttomanTechs/pardus-yol-arkadasi/releases/latest/download/pardus-yol-arkadasi_1.0.0_all.deb
   ```

2. **Paketi Kurun**
   ```bash
   sudo dpkg -i pardus-yol-arkadasi_1.0.0_all.deb
   ```

3. **Bağımlılıkları Yükleyin**
   ```bash
   sudo apt-get install -f
   ```

4. **Kurulumu Doğrulayın**
   ```bash
   pardus-yol-arkadasi --version
   ```

### Yöntem 2: Kaynak Koddan Kurulum

1. **Depoyu Klonlayın**
   ```bash
   git clone https://github.com/OttomanTechs/pardus-yol-arkadasi.git
   cd pardus-yol-arkadasi
   ```

2. **Bağımlılıkları Yükleyin**
   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-pyqt5 python3-pyqt5.qtmultimedia
   ```

3. **Uygulamayı Çalıştırın**
   ```bash
   python3 src/main.py
   ```

### Yöntem 3: Geliştirici Kurulumu

1. **Geliştirme Araçlarını Yükleyin**
   ```bash
   sudo apt-get install python3-pip python3-venv git
   ```

2. **Depoyu Klonlayın**
   ```bash
   git clone https://github.com/OttomanTechs/pardus-yol-arkadasi.git
   cd pardus-yol-arkadasi
   ```

3. **Sanal Ortam Oluşturun**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Bağımlılıkları Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

5. **Geliştirme Modunda Çalıştırın**
   ```bash
   ./run-dev.sh
   ```

## 🚀 İlk Çalıştırma

### Masaüstünden Başlatma

Kurulumdan sonra:
1. Uygulama Menüsü > Eğitim > Pardus Yol Arkadaşı
2. Veya masaüstündeki ikona çift tıklayın

### Komut Satırından Başlatma

```bash
pardus-yol-arkadasi
```

### Komut Satırı Seçenekleri

```bash
# Debug modunda çalıştır
pardus-yol-arkadasi --debug

# Belirli bir rehberi başlat
pardus-yol-arkadasi --tutorial desktop-basics

# Tam ekran modunda başlat
pardus-yol-arkadasi --fullscreen

# Otomatik başlatmayı devre dışı bırak
pardus-yol-arkadasi --no-autostart

# Yardım
pardus-yol-arkadasi --help
```

## 🔧 Sorun Giderme

### PyQt5 Bulunamadı Hatası

```bash
sudo apt-get install python3-pyqt5 python3-pyqt5.qtmultimedia
```

### Ses Çalmıyor

```bash
sudo apt-get install gstreamer1.0-plugins-good gstreamer1.0-plugins-bad
```

### İkon Görünmüyor

```bash
sudo gtk-update-icon-cache -f -t /usr/share/pixmaps
```

### Uygulama Açılmıyor

1. Terminal'den çalıştırıp hata mesajını kontrol edin:
   ```bash
   pardus-yol-arkadasi --debug
   ```

2. Log dosyasını kontrol edin:
   ```bash
   cat ~/.config/pardus-yol-arkadasi/pardus-yol-arkadasi.log
   ```

3. Yapılandırmayı sıfırlayın:
   ```bash
   rm -rf ~/.config/pardus-yol-arkadasi
   ```

## 🗑️ Kaldırma

### Debian Paketi ile Kurulmuşsa

```bash
sudo apt-get remove pardus-yol-arkadasi
```

### Yapılandırma Dosyalarını da Silmek İçin

```bash
sudo apt-get purge pardus-yol-arkadasi
rm -rf ~/.config/pardus-yol-arkadasi
```

## 🔄 Güncelleme

### Debian Paketi ile

```bash
# Yeni paketi indirin
wget https://github.com/OttomanTechs/pardus-yol-arkadasi/releases/latest/download/pardus-yol-arkadasi_1.0.0_all.deb

# Güncelleyin
sudo dpkg -i pardus-yol-arkadasi_1.0.0_all.deb
```

### Kaynak Koddan

```bash
cd pardus-yol-arkadasi
git pull origin main
python3 src/main.py
```

## 📞 Destek

Sorun yaşıyorsanız:
- **GitHub Issues**: https://github.com/OttomanTechs/pardus-yol-arkadasi/issues
- **E-posta**: ottoman.techs@example.com
- **Dokümantasyon**: https://github.com/OttomanTechs/pardus-yol-arkadasi/wiki

## 📝 Notlar

- İlk çalıştırmada otomatik başlatma ayarı yapılır
- Yapılandırma dosyaları `~/.config/pardus-yol-arkadasi/` dizininde saklanır
- Rehber ilerleme durumu otomatik kaydedilir
- Akıllı tahtalarda tam ekran modu önerilir
