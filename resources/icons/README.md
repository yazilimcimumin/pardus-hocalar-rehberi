# İkonlar

Bu dizinde uygulama ikonları bulunur.

## 📁 Mevcut İkonlar

- `icon512.png` - Orijinal ikon (512x512 px)
- `app_icon.png` - Ana uygulama ikonu (512x512 px)
- `app_icon_16.png` - Küçük ikon (16x16 px)
- `app_icon_32.png` - Küçük ikon (32x32 px)
- `app_icon_48.png` - Orta ikon (48x48 px)
- `app_icon_64.png` - Orta ikon (64x64 px)
- `app_icon_128.png` - Büyük ikon (128x128 px)
- `app_icon_256.png` - Büyük ikon (256x256 px)

## 🔧 İkon Boyutlandırma

Yeni bir ikon eklemek için:

1. **512x512 boyutunda PNG dosyasını `icon512.png` olarak kaydedin**
2. **Boyutlandırma scriptini çalıştırın:**
   ```bash
   cd resources/icons
   ./resize_icons.sh
   ```

Script otomatik olarak tüm boyutları oluşturacaktır.

## 📝 Manuel Boyutlandırma

ImageMagick ile manuel boyutlandırma:

```bash
# Tek boyut
convert icon512.png -resize 64x64 app_icon_64.png

# Birden fazla boyut
for size in 16 32 48 64 128 256; do
    convert icon512.png -resize ${size}x${size} app_icon_${size}.png
done
```

## 🎨 İkon Tasarım Önerileri

- **Basit ve Anlaşılır**: Küçük boyutlarda da tanınabilir olmalı
- **Yüksek Kontrast**: Arka plandan ayrılmalı
- **Pardus Teması**: Mavi/yeşil tonları kullanın
- **Şeffaf Arka Plan**: PNG formatında alfa kanalı
- **Keskin Kenarlar**: Bulanık olmayan, net çizgiler

## 📦 Paket İçinde Kullanım

Debian paketi oluşturulurken:
- `app_icon.png` → `/usr/share/pixmaps/pardus-yol-arkadasi.png`
- Farklı boyutlar → `/usr/share/icons/hicolor/[boyut]/apps/`

## ✅ İkon Kontrolü

İkonların doğru oluşturulduğunu kontrol edin:

```bash
# Dosya boyutlarını göster
ls -lh app_icon*.png

# İkon boyutlarını kontrol et
file app_icon*.png

# Görsel olarak kontrol et
eog app_icon.png  # veya ristretto app_icon.png
```

## 🔄 Güncelleme

İkon değiştiğinde:
1. Yeni `icon512.png` dosyasını koyun
2. `./resize_icons.sh` çalıştırın
3. Paketi yeniden oluşturun: `../../build-deb.sh`
