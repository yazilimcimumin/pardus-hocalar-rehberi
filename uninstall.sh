#!/bin/bash
# Kaldırma Scripti
# Ottoman Techs - Teknofest 2026

set -e

echo "========================================="
echo "Pardus Yol Arkadaşı - Kaldırma"
echo "========================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Root kontrolü
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}HATA:${NC} Bu script root olarak çalıştırılmalı"
    echo "Kullanım: sudo bash uninstall.sh"
    exit 1
fi

# Onay iste
echo -e "${YELLOW}UYARI:${NC} Pardus Yol Arkadaşı kaldırılacak."
read -p "Devam etmek istiyor musunuz? (e/h): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Ee]$ ]]; then
    echo "İptal edildi."
    exit 0
fi

echo ""
echo -e "${YELLOW}[1/4]${NC} Çalışan uygulama kapatılıyor..."
if pgrep -f "pardus-yol-arkadasi" > /dev/null; then
    pkill -f "pardus-yol-arkadasi" || true
    echo -e "${GREEN}✓${NC} Uygulama kapatıldı"
else
    echo -e "${GREEN}✓${NC} Uygulama zaten çalışmıyor"
fi
echo ""

echo -e "${YELLOW}[2/4]${NC} Dosyalar siliniyor..."
rm -rf /usr/share/pardus-yol-arkadasi
rm -f /usr/bin/pardus-yol-arkadasi
rm -f /usr/share/applications/pardus-yol-arkadasi.desktop
rm -f /usr/share/pixmaps/pardus-yol-arkadasi.png
echo -e "${GREEN}✓${NC} Dosyalar silindi"
echo ""

echo -e "${YELLOW}[3/4]${NC} Kullanıcı ayarları siliniyor..."
for user_home in /home/*; do
    if [ -d "$user_home/.config/pardus-yol-arkadasi" ]; then
        rm -rf "$user_home/.config/pardus-yol-arkadasi"
        echo -e "${GREEN}✓${NC} $(basename $user_home) kullanıcısının ayarları silindi"
    fi
done
echo ""

echo -e "${YELLOW}[4/4]${NC} Desktop database güncelleniyor..."
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database -q /usr/share/applications
fi
echo -e "${GREEN}✓${NC} Güncelleme tamamlandı"
echo ""

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}Kaldırma başarıyla tamamlandı!${NC}"
echo -e "${GREEN}=========================================${NC}"
echo ""
