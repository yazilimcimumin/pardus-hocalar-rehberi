# Pardus Yol Arkadaşı - Hızlı Başlangıç Kılavuzu

## 🚀 5 Dakikada Başlayın

### 1. Kurulum (2 dakika)

```bash
# Paketi indirin
wget https://github.com/OttomanTechs/pardus-yol-arkadasi/releases/latest/download/pardus-yol-arkadasi_1.0.0_all.deb

# Kurun
sudo dpkg -i pardus-yol-arkadasi_1.0.0_all.deb
sudo apt-get install -f
```

### 2. İlk Çalıştırma (1 dakika)

Uygulama Menüsü > Eğitim > **Pardus Yol Arkadaşı**

veya

```bash
pardus-yol-arkadasi
```

### 3. Rehber Seçin (2 dakika)

Sol panelden bir rehber seçin:
- 📚 **Masaüstü Temelleri** - Yeni başlayanlar için
- 📁 **Dosya İşlemleri** - Dosya yönetimi
- 🖥️ **Akıllı Tahta** - Dokunmatik ekran kullanımı

## 🎯 Öğretmenler İçin Önerilen Sıra

1. **Masaüstü Temelleri** (15 dk) - Pardus arayüzünü tanıyın
2. **Dosya İşlemleri** (20 dk) - Dosya yönetimini öğrenin
3. **Ofis Uygulamaları** (25 dk) - LibreOffice kullanımı
4. **Akıllı Tahta** (30 dk) - Dokunmatik ekran ve bakım
5. **İnternet ve E-posta** (20 dk) - İletişim araçları

## 💡 İpuçları

### Rehber Sırasında
- **Space** veya **Sonraki** butonu ile ilerleyin
- **Geri** butonu ile önceki adıma dönün
- **Atla** butonu ile rehberi atlayın
- **ESC** tuşu ile rehberi kapatın

### Klavye Kısayolları
- `Ctrl+Q` - Uygulamayı kapat
- `F11` - Tam ekran
- `F1` - Yardım

### Akıllı Tahta Kullanıcıları
- Tam ekran modunda başlatın: `pardus-yol-arkadasi --fullscreen`
- Ekran klavyesini etkinleştirin (Ayarlar > Erişilebilirlik)
- Dokunmatik kalibrasyonu yapın (Terminal > `xinput_calibrator`)

## 🔧 Hızlı Sorun Giderme

### Uygulama Açılmıyor
```bash
# Bağımlılıkları kontrol edin
sudo apt-get install python3-pyqt5 python3-pyqt5.qtmultimedia

# Debug modunda çalıştırın
pardus-yol-arkadasi --debug
```

### Ses Çalmıyor
```bash
sudo apt-get install gstreamer1.0-plugins-good
```

### Dokunmatik Çalışmıyor
```bash
# Kalibrasyon yapın
xinput_calibrator

# Veya yeniden başlatın
sudo reboot
```

## 📖 Daha Fazla Bilgi

- **Detaylı Kurulum**: [INSTALLATION.md](INSTALLATION.md)
- **Katkıda Bulunma**: [CONTRIBUTING.md](../CONTRIBUTING.md)
- **GitHub**: https://github.com/OttomanTechs/pardus-yol-arkadasi
- **Destek**: ottoman.techs@example.com

## 🎓 Eğitim Materyalleri

### Video Rehberler (Yakında)
- Pardus Yol Arkadaşı Tanıtımı
- Akıllı Tahta Kullanımı
- Ofis Uygulamaları ile Ders Hazırlama

### PDF Kılavuzlar (Yakında)
- Öğretmen El Kitabı
- Akıllı Tahta Bakım Rehberi
- Hızlı Referans Kartı

## 🤝 Topluluk

- **Forum**: https://forum.pardus.org.tr
- **Telegram**: @PardusYolArkadasi
- **E-posta Listesi**: pardus-yol-arkadasi@googlegroups.com

## 📝 Geri Bildirim

Görüşleriniz bizim için değerli:
- GitHub Issues: Hata bildirimi ve özellik önerisi
- E-posta: ottoman.techs@example.com
- Anket: https://forms.gle/xxxxx (yakında)

---

**Pardus Yol Arkadaşı** - Windows'tan Pardus'a geçişi kolaylaştırıyoruz! 🚀
