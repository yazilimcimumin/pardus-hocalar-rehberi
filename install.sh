#!/bin/bash
# Basit Kurulum Scripti (Debian paketi olmadan)
# Ottoman Techs - Teknofest 2026

set -e

echo "========================================="
echo "Pardus Yol Arkadaşı - Basit Kurulum"
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
    echo "Kullanım: sudo bash install.sh"
    exit 1
fi

# Python kontrolü
echo -e "${YELLOW}[1/5]${NC} Python kontrolü..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}HATA:${NC} Python 3 bulunamadı!"
    exit 1
fi
echo -e "${GREEN}✓${NC} Python bulundu"
echo ""

# PyQt5 kurulumu
echo -e "${YELLOW}[2/5]${NC} PyQt5 kurulumu..."
apt-get update -qq
apt-get install -y python3-pyqt5 python3-pyqt5.qtmultimedia
echo -e "${GREEN}✓${NC} PyQt5 kuruldu"
echo ""

# Dosyaları kopyala
echo -e "${YELLOW}[3/5]${NC} Dosyalar kopyalanıyor..."
mkdir -p /usr/share/pardus-yol-arkadasi
cp -r src/* /usr/share/pardus-yol-arkadasi/
cp -r resources /usr/share/pardus-yol-arkadasi/
echo -e "${GREEN}✓${NC} Dosyalar kopyalandı"
echo ""

# Çalıştırılabilir script oluştur
echo -e "${YELLOW}[4/5]${NC} Çalıştırılabilir script oluşturuluyor..."
cat > /usr/bin/pardus-yol-arkadasi << 'EOF'
#!/bin/bash
cd /usr/share/pardus-yol-arkadasi
python3 main.py "$@"
EOF
chmod +x /usr/bin/pardus-yol-arkadasi
echo -e "${GREEN}✓${NC} Script oluşturuldu"
echo ""

# Masaüstü dosyası oluştur
echo -e "${YELLOW}[5/5]${NC} Masaüstü kısayolu oluşturuluyor..."
mkdir -p /usr/share/applications
cat > /usr/share/applications/pardus-yol-arkadasi.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Pardus Yol Arkadaşı
Name[tr]=Pardus Yol Arkadaşı
Comment=İnteraktif Pardus kullanıcı rehberi
Comment[tr]=İnteraktif Pardus kullanıcı rehberi
GenericName=Kullanıcı Rehberi
GenericName[tr]=Kullanıcı Rehberi
Exec=pardus-yol-arkadasi
Icon=/usr/share/pardus-yol-arkadasi/resources/icons/app_icon.png
Terminal=false
Categories=Education;System;
Keywords=pardus;rehber;tutorial;guide;onboarding;yardım;help;
StartupNotify=true
EOF

# İkon kopyala
if [ -f "resources/icons/app_icon.png" ]; then
    cp resources/icons/app_icon.png /usr/share/pixmaps/pardus-yol-arkadasi.png
fi

# Desktop database güncelle
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database -q /usr/share/applications
fi

echo -e "${GREEN}✓${NC} Masaüstü kısayolu oluşturuldu"
echo ""

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}Kurulum başarıyla tamamlandı!${NC}"
echo -e "${GREEN}=========================================${NC}"
echo ""
echo "Uygulamayı başlatmak için:"
echo -e "  ${YELLOW}pardus-yol-arkadasi${NC}"
echo ""
echo "veya"
echo ""
echo "  Uygulama Menüsü > Eğitim > Pardus Yol Arkadaşı"
echo ""
