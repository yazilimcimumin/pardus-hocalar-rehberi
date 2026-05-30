#!/bin/bash
# Geliştirme ortamında uygulamayı çalıştırma scripti
# Ottoman Techs - Teknofest 2026

set -e

echo "========================================="
echo "Pardus Yol Arkadaşı - Geliştirme Modu"
echo "========================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Python kontrolü
echo -e "${YELLOW}[1/3]${NC} Python kontrolü..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}HATA:${NC} Python 3 bulunamadı!"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION bulundu"
echo ""

# PyQt5 kontrolü
echo -e "${YELLOW}[2/3]${NC} PyQt5 kontrolü..."
if ! python3 -c "import PyQt5" 2>/dev/null; then
    echo -e "${RED}HATA:${NC} PyQt5 yüklü değil!"
    echo "Yüklemek için: sudo apt-get install python3-pyqt5 python3-pyqt5.qtmultimedia"
    exit 1
fi
echo -e "${GREEN}✓${NC} PyQt5 yüklü"
echo ""

# Uygulamayı başlat
echo -e "${YELLOW}[3/3]${NC} Uygulama başlatılıyor..."
echo ""

cd src
python3 main.py --debug "$@"
