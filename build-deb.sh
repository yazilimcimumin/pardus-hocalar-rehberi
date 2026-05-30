#!/bin/bash
# Debian paketi oluşturma scripti
# Ottoman Techs - Teknofest 2026

set -e

echo "========================================="
echo "Pardus Yol Arkadaşı - Paket Oluşturma"
echo "========================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Gerekli araçları kontrol et
echo -e "${YELLOW}[1/5]${NC} Gerekli araçlar kontrol ediliyor..."

if ! command -v dpkg-buildpackage &> /dev/null; then
    echo -e "${RED}HATA:${NC} dpkg-buildpackage bulunamadı!"
    echo "Lütfen şu komutu çalıştırın: sudo apt-get install dpkg-dev"
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}HATA:${NC} python3 bulunamadı!"
    exit 1
fi

echo -e "${GREEN}✓${NC} Tüm gerekli araçlar mevcut"
echo ""

# Eski build dosyalarını temizle
echo -e "${YELLOW}[2/5]${NC} Eski build dosyaları temizleniyor..."
rm -rf build/ dist/ *.egg-info/
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
echo -e "${GREEN}✓${NC} Temizlik tamamlandı"
echo ""

# Bağımlılıkları kontrol et
echo -e "${YELLOW}[3/5]${NC} Python bağımlılıkları kontrol ediliyor..."
if ! python3 -c "import PyQt5" 2>/dev/null; then
    echo -e "${YELLOW}UYARI:${NC} PyQt5 yüklü değil. Paket çalışmayabilir."
    echo "Yüklemek için: sudo apt-get install python3-pyqt5"
fi
echo -e "${GREEN}✓${NC} Bağımlılık kontrolü tamamlandı"
echo ""

# Debian paketi oluştur
echo -e "${YELLOW}[4/5]${NC} Debian paketi oluşturuluyor..."
dpkg-buildpackage -us -uc -b

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Paket başarıyla oluşturuldu"
else
    echo -e "${RED}HATA:${NC} Paket oluşturma başarısız!"
    exit 1
fi
echo ""

# Paket bilgilerini göster
echo -e "${YELLOW}[5/5]${NC} Paket bilgileri:"
echo ""

DEB_FILE=$(ls -t ../*.deb 2>/dev/null | head -1)

if [ -f "$DEB_FILE" ]; then
    echo -e "${GREEN}Paket dosyası:${NC} $DEB_FILE"
    echo -e "${GREEN}Paket boyutu:${NC} $(du -h "$DEB_FILE" | cut -f1)"
    echo ""
    echo "Paket içeriği:"
    dpkg-deb --info "$DEB_FILE" | grep -A 20 "Package:"
    echo ""
    echo -e "${GREEN}=========================================${NC}"
    echo -e "${GREEN}Paket başarıyla oluşturuldu!${NC}"
    echo -e "${GREEN}=========================================${NC}"
    echo ""
    echo "Kurulum için:"
    echo -e "  ${YELLOW}sudo dpkg -i $DEB_FILE${NC}"
    echo -e "  ${YELLOW}sudo apt-get install -f${NC}"
    echo ""
    echo "Test için:"
    echo -e "  ${YELLOW}pardus-yol-arkadasi${NC}"
    echo ""
else
    echo -e "${RED}HATA:${NC} Paket dosyası bulunamadı!"
    exit 1
fi
