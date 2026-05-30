#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Ana Uygulama
Ottoman Techs - Teknofest 2026

Bu uygulama, Pardus işletim sistemine yeni geçen kullanıcılar için
interaktif bir rehberlik sistemi sağlar.
"""

import sys
import os
import argparse
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QTranslator, QLocale
from PyQt5.QtGui import QIcon

# Proje modüllerini içe aktar
from ui.main_window import MainWindow
from core.config import Config


def setup_application():
    """
    Uygulama başlangıç ayarlarını yapılandır
    """
    # Yüksek DPI desteği (akıllı tahtalar için önemli)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # Uygulama örneğini oluştur
    app = QApplication(sys.argv)
    
    # Uygulama bilgilerini ayarla
    app.setApplicationName("Pardus Yol Arkadaşı")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Ottoman Techs")
    app.setOrganizationDomain("ottomantechs.com")
    
    # Uygulama ikonunu ayarla
    icon_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "resources",
        "icons",
        "app_icon.png"
    )
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    return app


def parse_arguments():
    """
    Komut satırı argümanlarını işle
    """
    parser = argparse.ArgumentParser(
        description="Pardus Yol Arkadaşı - İnteraktif Kullanıcı Rehberi"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Debug modunda çalıştır (detaylı log çıktısı)"
    )
    
    parser.add_argument(
        "--tutorial",
        type=str,
        help="Belirli bir rehberi doğrudan başlat (örn: desktop-basics)"
    )
    
    parser.add_argument(
        "--no-autostart",
        action="store_true",
        help="Otomatik başlatma ayarını devre dışı bırak"
    )
    
    parser.add_argument(
        "--fullscreen",
        action="store_true",
        help="Tam ekran modunda başlat (akıllı tahta için)"
    )
    
    return parser.parse_args()


def check_first_run():
    """
    Uygulamanın ilk kez çalıştırılıp çalıştırılmadığını kontrol et
    
    Returns:
        bool: İlk çalıştırma ise True, değilse False
    """
    config = Config()
    return config.is_first_run()


def main():
    """
    Ana uygulama giriş noktası
    """
    # Komut satırı argümanlarını işle
    args = parse_arguments()
    
    # Debug modu ayarla
    if args.debug:
        os.environ["PARDUS_YOL_ARKADASI_DEBUG"] = "1"
        print("[DEBUG] Debug modu aktif")
    
    # Uygulamayı başlat
    app = setup_application()
    
    # Yapılandırmayı yükle
    config = Config()
    
    # İlk çalıştırma kontrolü
    is_first_run = check_first_run()
    if is_first_run and args.debug:
        print("[DEBUG] İlk çalıştırma tespit edildi")
    
    # Ana pencereyi oluştur
    main_window = MainWindow(
        debug=args.debug,
        start_tutorial=args.tutorial,
        is_first_run=is_first_run
    )
    
    # Tam ekran modu
    if args.fullscreen or config.get("display.fullscreen_on_start", False):
        main_window.showFullScreen()
    else:
        main_window.show()
    
    # Otomatik başlatma ayarı
    if args.no_autostart:
        config.set("autostart.enabled", False)
        if args.debug:
            print("[DEBUG] Otomatik başlatma devre dışı bırakıldı")
    
    # İlk çalıştırma bayrağını güncelle
    if is_first_run:
        config.set("first_run", False)
        config.save()
    
    # Uygulama döngüsünü başlat
    try:
        exit_code = app.exec_()
    except KeyboardInterrupt:
        print("\n[INFO] Uygulama kullanıcı tarafından sonlandırıldı")
        exit_code = 0
    
    # Temizlik işlemleri
    if args.debug:
        print("[DEBUG] Uygulama kapatılıyor...")
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
