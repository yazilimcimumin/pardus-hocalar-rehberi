#!/bin/bash
# Basit bir uygulama ikonu oluşturma scripti
# Ottoman Techs - Teknofest 2026

# ImageMagick gerekli
if ! command -v convert &> /dev/null; then
    echo "ImageMagick kurulu değil. Kurmak için:"
    echo "sudo apt-get install imagemagick"
    exit 1
fi

# 512x512 boyutunda basit bir ikon oluştur
convert -size 512x512 xc:none \
    -fill "#007aff" -draw "circle 256,256 256,50" \
    -fill white -font "DejaVu-Sans-Bold" -pointsize 200 \
    -gravity center -annotate +0+0 "P" \
    app_icon.png

echo "✓ app_icon.png oluşturuldu (512x512)"

# Farklı boyutlarda ikonlar oluştur
for size in 16 32 48 64 128 256; do
    convert app_icon.png -resize ${size}x${size} app_icon_${size}.png
    echo "✓ app_icon_${size}.png oluşturuldu"
done

echo ""
echo "Tüm ikonlar başarıyla oluşturuldu!"
echo "Ana ikon: app_icon.png (512x512)"
