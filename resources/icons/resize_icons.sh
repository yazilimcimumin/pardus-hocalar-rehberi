#!/bin/bash
# İkon boyutlandırma scripti
# Ottoman Techs - Teknofest 2026

set -e

echo "========================================="
echo "Pardus Yol Arkadaşı - İkon Boyutlandırma"
echo "========================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# ImageMagick kontrolü
if ! command -v convert &> /dev/null; then
    echo -e "${RED}HATA:${NC} ImageMagick kurulu değil!"
    echo "Kurmak için: sudo apt-get install imagemagick"
    exit 1
fi

# Kaynak dosya kontrolü
if [ ! -f "icon512.png" ]; then
    echo -e "${RED}HATA:${NC} icon512.png bulunamadı!"
    echo "Lütfen icon512.png dosyasını bu dizine koyun."
    exit 1
fi

echo -e "${YELLOW}[1/3]${NC} Kaynak ikon: icon512.png (512x512)"
echo ""

# Ana ikon olarak kopyala
echo -e "${YELLOW}[2/3]${NC} Ana ikon oluşturuluyor..."
cp icon512.png app_icon.png
echo -e "${GREEN}✓${NC} app_icon.png oluşturuldu (512x512)"
echo ""

# Farklı boyutlarda ikonlar oluştur
echo -e "${YELLOW}[3/3]${NC} Farklı boyutlar oluşturuluyor..."

sizes=(16 32 48 64 128 256)

for size in "${sizes[@]}"; do
    convert icon512.png -resize ${size}x${size} app_icon_${size}.png
    echo -e "${GREEN}✓${NC} app_icon_${size}.png oluşturuldu (${size}x${size})"
done

echo ""
echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}Tüm ikonlar başarıyla oluşturuldu!${NC}"
echo -e "${GREEN}=========================================${NC}"
echo ""
echo "Oluşturulan dosyalar:"
ls -lh app_icon*.png | awk '{print "  " $9 " - " $5}'
echo ""
echo "Kullanım:"
echo "  - app_icon.png: Ana uygulama ikonu (512x512)"
echo "  - app_icon_*.png: Farklı boyutlar (sistem ikonları için)"
