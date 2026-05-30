#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Ana Pencere
Ottoman Techs - Teknofest 2026

Uygulamanın ana penceresi ve rehber koordinasyonu.
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QListWidget, QListWidgetItem,
                             QStackedWidget, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QFont, QIcon, QScreen

from ui.spotlight import SpotlightWidget
from ui.tutorial_widget import TutorialWidget
from core.tutorial_manager import TutorialManager
from core.audio_manager import AudioManager
from core.config import Config


class MainWindow(QMainWindow):
    """
    Ana uygulama penceresi
    """
    
    def __init__(self, debug=False, start_tutorial=None, is_first_run=False):
        """
        Ana pencereyi başlat
        
        Args:
            debug (bool): Debug modu
            start_tutorial (str): Başlangıçta başlatılacak rehber
            is_first_run (bool): İlk çalıştırma mı?
        """
        super().__init__()
        
        self.debug = debug
        self.is_first_run = is_first_run
        
        # Yöneticileri başlat
        self.config = Config()
        self.tutorial_manager = TutorialManager()
        self.audio_manager = AudioManager()
        
        # Spotlight widget'ı
        self.spotlight = None
        self.tutorial_widget = None
        
        # UI'ı oluştur
        self._setup_ui()
        self._load_tutorials()
        
        # İlk çalıştırma kontrolü
        if is_first_run:
            self._show_welcome_message()
        
        # Belirli bir rehber başlatılacaksa
        if start_tutorial:
            QTimer.singleShot(500, lambda: self._start_tutorial_by_id(start_tutorial))
    
    def _setup_ui(self):
        """
        Kullanıcı arayüzünü oluştur
        """
        self.setWindowTitle("Pardus Yol Arkadaşı")
        self.setMinimumSize(900, 600)
        
        # Merkezi widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Ana layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sol panel - Rehber listesi
        left_panel = self._create_left_panel()
        main_layout.addWidget(left_panel, 1)
        
        # Sağ panel - Rehber detayları
        right_panel = self._create_right_panel()
        main_layout.addWidget(right_panel, 2)
        
        # Pencereyi ekranın ortasına yerleştir
        self._center_window()
        
        # Stil uygula
        self._apply_styles()
    
    def _create_left_panel(self):
        """
        Sol paneli oluştur (rehber listesi)
        
        Returns:
            QWidget: Sol panel widget'ı
        """
        panel = QWidget()
        panel.setObjectName("leftPanel")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Başlık
        title = QLabel("📚 Rehberler")
        title.setObjectName("panelTitle")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Arama çubuğu
        from PyQt5.QtWidgets import QLineEdit
        self.search_box = QLineEdit()
        self.search_box.setObjectName("searchBox")
        self.search_box.setPlaceholderText("🔍 Rehberlerde ara...")
        self.search_box.textChanged.connect(self._on_search_changed)
        self.search_box.setClearButtonEnabled(True)
        search_font = QFont()
        search_font.setPointSize(12)
        self.search_box.setFont(search_font)
        layout.addWidget(self.search_box)
        
        # Rehber listesi
        self.tutorial_list = QListWidget()
        self.tutorial_list.setObjectName("tutorialList")
        self.tutorial_list.itemClicked.connect(self._on_tutorial_selected)
        layout.addWidget(self.tutorial_list)
        
        # Alt butonlar
        button_layout = QVBoxLayout()
        button_layout.setSpacing(10)
        
        self.settings_button = QPushButton("⚙️ Ayarlar")
        self.settings_button.setObjectName("settingsButton")
        self.settings_button.clicked.connect(self._show_settings)
        
        self.about_button = QPushButton("ℹ️ Hakkında")
        self.about_button.setObjectName("aboutButton")
        self.about_button.clicked.connect(self._show_about)
        
        button_layout.addWidget(self.settings_button)
        button_layout.addWidget(self.about_button)
        
        layout.addLayout(button_layout)
        
        return panel
    
    def _create_right_panel(self):
        """
        Sağ paneli oluştur (rehber detayları)
        
        Returns:
            QWidget: Sağ panel widget'ı
        """
        panel = QWidget()
        panel.setObjectName("rightPanel")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Başlık
        self.detail_title = QLabel("Rehber Seçin")
        self.detail_title.setObjectName("detailTitle")
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.detail_title.setFont(title_font)
        layout.addWidget(self.detail_title)
        
        # Açıklama
        self.detail_description = QLabel(
            "Sol taraftan bir rehber seçerek Pardus'u öğrenmeye başlayın."
        )
        self.detail_description.setObjectName("detailDescription")
        self.detail_description.setWordWrap(True)
        desc_font = QFont()
        desc_font.setPointSize(12)
        self.detail_description.setFont(desc_font)
        layout.addWidget(self.detail_description)
        
        # Bilgi etiketleri
        info_layout = QHBoxLayout()
        
        self.difficulty_label = QLabel("")
        self.difficulty_label.setObjectName("infoLabel")
        
        self.time_label = QLabel("")
        self.time_label.setObjectName("infoLabel")
        
        info_layout.addWidget(self.difficulty_label)
        info_layout.addWidget(self.time_label)
        info_layout.addStretch()
        
        layout.addLayout(info_layout)
        
        layout.addStretch()
        
        # Başlat butonu
        self.start_button = QPushButton("🚀 Rehberi Başlat")
        self.start_button.setObjectName("startButton")
        self.start_button.setFixedHeight(60)
        self.start_button.clicked.connect(self._start_selected_tutorial)
        self.start_button.setEnabled(False)
        
        button_font = QFont()
        button_font.setPointSize(14)
        button_font.setBold(True)
        self.start_button.setFont(button_font)
        
        layout.addWidget(self.start_button)
        
        return panel
    
    def _apply_styles(self):
        """
        Uygulama stillerini uygula - Apple tarzı modern tasarım
        """
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #f5f5f7, stop:1 #e8e8ed);
            }
            
            #leftPanel {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #2c2c2e, stop:1 #1c1c1e);
                border-right: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            #rightPanel {
                background-color: #ffffff;
                border-radius: 16px;
                margin: 10px;
            }
            
            #panelTitle {
                color: #f5f5f7;
                padding: 15px;
                font-size: 20pt;
                font-weight: 700;
                letter-spacing: -0.5px;
            }
            
            #tutorialList {
                background-color: transparent;
                color: #f5f5f7;
                border: none;
                padding: 8px;
                font-size: 14pt;
                font-weight: 500;
            }
            
            #tutorialList::item {
                padding: 16px 12px;
                border-radius: 10px;
                margin: 4px 0px;
                color: #f5f5f7;
            }
            
            #tutorialList::item:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
            
            #tutorialList::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #007aff, stop:1 #0051d5);
                color: white;
                font-weight: 600;
            }
            
            #detailTitle {
                color: #1d1d1f;
                font-size: 34pt;
                font-weight: 700;
                letter-spacing: -1.2px;
                line-height: 1.1;
            }
            
            #detailDescription {
                color: #6e6e73;
                font-size: 15pt;
                line-height: 1.6;
                letter-spacing: -0.3px;
            }
            
            #infoLabel {
                color: #6e6e73;
                font-size: 12pt;
                font-weight: 500;
                padding: 10px 18px;
                background-color: #f5f5f7;
                border-radius: 20px;
                border: 1px solid #e8e8ed;
            }
            
            #startButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #34c759, stop:1 #30b350);
                color: white;
                border: none;
                border-radius: 14px;
                padding: 18px;
                font-size: 17pt;
                font-weight: 600;
                letter-spacing: -0.4px;
            }
            
            #startButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #30b350, stop:1 #2a9d46);
            }
            
            #startButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #2a9d46, stop:1 #248a3d);
                padding: 19px 18px 17px 18px;
            }
            
            #startButton:disabled {
                background: #d1d1d6;
                color: #8e8e93;
            }
            
            #settingsButton, #aboutButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: #f5f5f7;
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 10px;
                padding: 14px;
                font-size: 14pt;
                font-weight: 500;
            }
            
            #settingsButton:hover, #aboutButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
                border: 1px solid rgba(255, 255, 255, 0.25);
            }
            
            #settingsButton:pressed, #aboutButton:pressed {
                background-color: rgba(255, 255, 255, 0.05);
            }
        """)
    
    def _center_window(self):
        """
        Pencereyi ekranın ortasına yerleştir
        """
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())
    
    def _load_tutorials(self):
        """
        Rehberleri listeye yükle
        """
        self.tutorial_list.clear()
        
        tutorials = self.tutorial_manager.get_all_tutorials()
        
        if not tutorials:
            item = QListWidgetItem("Rehber bulunamadı")
            item.setFlags(Qt.NoItemFlags)
            self.tutorial_list.addItem(item)
            return
        
        for tutorial in tutorials:
            # Tamamlanma durumunu kontrol et
            completed = self.config.is_tutorial_completed(tutorial.id)
            prefix = "✓ " if completed else "○ "
            
            item_text = f"{prefix}{tutorial.title}"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, tutorial.id)
            self.tutorial_list.addItem(item)
    
    def _on_tutorial_selected(self, item):
        """
        Rehber seçildiğinde çağrılır
        
        Args:
            item: Seçilen liste öğesi
        """
        tutorial_id = item.data(Qt.UserRole)
        if not tutorial_id:
            return
        
        tutorial = self.tutorial_manager.get_tutorial(tutorial_id)
        if not tutorial:
            return
        
        # Detayları güncelle
        self.detail_title.setText(tutorial.title)
        self.detail_description.setText(tutorial.description)
        
        # Zorluk seviyesi
        difficulty_map = {
            "beginner": "🟢 Başlangıç",
            "intermediate": "🟡 Orta",
            "advanced": "🔴 İleri"
        }
        self.difficulty_label.setText(
            difficulty_map.get(tutorial.difficulty, "○ Bilinmiyor")
        )
        
        # Tahmini süre
        self.time_label.setText(f"⏱️ ~{tutorial.estimated_time} dakika")
        
        # Başlat butonunu aktif et
        self.start_button.setEnabled(True)
        self.selected_tutorial_id = tutorial_id
    
    def _start_selected_tutorial(self):
        """
        Seçili rehberi başlat
        """
        if hasattr(self, 'selected_tutorial_id'):
            self._start_tutorial_by_id(self.selected_tutorial_id)
    
    def _start_tutorial_by_id(self, tutorial_id):
        """
        Belirli bir rehberi başlat
        
        Args:
            tutorial_id (str): Rehber kimliği
        """
        if not self.tutorial_manager.start_tutorial(tutorial_id):
            QMessageBox.warning(
                self,
                "Hata",
                f"Rehber başlatılamadı: {tutorial_id}"
            )
            return
        
        # Ana pencereyi gizle
        self.hide()
        
        # Spotlight ve tutorial widget'larını oluştur
        self._create_overlay_widgets()
        
        # İlk adımı göster
        self._show_current_step()
    
    def _create_overlay_widgets(self):
        """
        Overlay widget'larını oluştur (spotlight ve tutorial)
        """
        # Spotlight widget'ı
        if self.spotlight is None:
            self.spotlight = SpotlightWidget()
            screen_geometry = QDesktopWidget().screenGeometry()
            self.spotlight.setGeometry(screen_geometry)
        
        # Tutorial widget'ı
        if self.tutorial_widget is None:
            self.tutorial_widget = TutorialWidget()
            self.tutorial_widget.next_clicked.connect(self._on_next_step)
            self.tutorial_widget.previous_clicked.connect(self._on_previous_step)
            self.tutorial_widget.skip_clicked.connect(self._on_skip_tutorial)
            self.tutorial_widget.close_clicked.connect(self._on_close_tutorial)
            
            # Tutorial widget'ı ekranın sağ alt köşesine yerleştir
            screen_geometry = QDesktopWidget().screenGeometry()
            x = screen_geometry.width() - self.tutorial_widget.width() - 50
            y = screen_geometry.height() - self.tutorial_widget.height() - 50
            self.tutorial_widget.move(x, y)
    
    def _show_current_step(self):
        """
        Mevcut rehber adımını göster
        """
        tutorial = self.tutorial_manager.get_current_tutorial()
        if not tutorial:
            return
        
        step = tutorial.get_current_step()
        if not step:
            self._finish_tutorial()
            return
        
        # Tutorial widget'ı güncelle
        self.tutorial_widget.set_tutorial_info(
            step.title,
            step.description,
            tutorial.current_step_index + 1,
            len(tutorial.steps)
        )
        
        # Spotlight'ı göster
        self.spotlight.show_spotlight()
        self.tutorial_widget.show_with_animation()
        
        # Hedef alanı vurgula (örnek koordinatlar)
        # Gerçek uygulamada, target selector'a göre gerçek widget bulunur
        if step.target:
            # Örnek: Ekranın ortasında bir alan
            screen_geometry = QDesktopWidget().screenGeometry()
            target_rect = QRect(
                screen_geometry.width() // 2 - 150,
                screen_geometry.height() // 2 - 100,
                300,
                200
            )
            self.spotlight.set_spotlight_target(target_rect, animated=True)
        
        # Ses dosyası varsa oynat
        if step.audio_file and self.config.get("audio.enabled", True):
            self.audio_manager.play(step.audio_file)
    
    def _on_next_step(self):
        """
        Sonraki adıma geç
        """
        tutorial = self.tutorial_manager.get_current_tutorial()
        if not tutorial:
            return
        
        if tutorial.next_step():
            self._show_current_step()
        else:
            self._finish_tutorial()
    
    def _on_previous_step(self):
        """
        Önceki adıma geç
        """
        tutorial = self.tutorial_manager.get_current_tutorial()
        if not tutorial:
            return
        
        if tutorial.previous_step():
            self._show_current_step()
    
    def _on_skip_tutorial(self):
        """
        Rehberi atla
        """
        reply = QMessageBox.question(
            self,
            "Rehberi Atla",
            "Bu rehberi atlamak istediğinizden emin misiniz?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self._close_tutorial()
    
    def _on_close_tutorial(self):
        """
        Rehberi kapat
        """
        self._close_tutorial()
    
    def _finish_tutorial(self):
        """
        Rehberi tamamla
        """
        tutorial = self.tutorial_manager.get_current_tutorial()
        if tutorial:
            # Tamamlandı olarak işaretle
            self.config.mark_tutorial_completed(tutorial.id)
            
            QMessageBox.information(
                self,
                "Tebrikler! 🎉",
                f"'{tutorial.title}' rehberini başarıyla tamamladınız!"
            )
        
        self._close_tutorial()
    
    def _close_tutorial(self):
        """
        Rehber overlay'ini kapat
        """
        # Sesi durdur
        self.audio_manager.stop()
        
        # Widget'ları gizle
        if self.spotlight:
            self.spotlight.hide_spotlight()
        
        if self.tutorial_widget:
            self.tutorial_widget.hide()
        
        # Rehberi durdur
        self.tutorial_manager.stop_tutorial()
        
        # Ana pencereyi göster
        self.show()
        
        # Rehber listesini güncelle
        self._load_tutorials()
    
    def _show_welcome_message(self):
        """
        İlk çalıştırma hoş geldin mesajı
        """
        QMessageBox.information(
            self,
            "Pardus Yol Arkadaşı'na Hoş Geldiniz! 👋",
            "Pardus işletim sistemini öğrenmenize yardımcı olmak için buradayız.\n\n"
            "Sol taraftan bir rehber seçerek başlayabilirsiniz.\n"
            "Her rehber, adım adım size yol gösterecektir."
        )
    
    def _show_settings(self):
        """
        Ayarlar penceresini göster
        """
        QMessageBox.information(
            self,
            "Ayarlar",
            "Ayarlar özelliği yakında eklenecek."
        )
    
    def _show_about(self):
        """
        Hakkında penceresini göster
        """
        QMessageBox.about(
            self,
            "Pardus Yol Arkadaşı Hakkında",
            "<h2>Pardus Yol Arkadaşı</h2>"
            "<p><b>Versiyon:</b> 1.0.0</p>"
            "<p><b>Geliştirici:</b> Ottoman Techs</p>"
            "<p><b>Yarışma:</b> Teknofest 2026 - Pardus Yarışması</p>"
            "<br>"
            "<p>Pardus işletim sistemine yeni geçen kullanıcılar için "
            "interaktif bir rehberlik sistemi.</p>"
            "<br>"
            "<p>© 2026 Ottoman Techs. Tüm hakları saklıdır.</p>"
        )
    
    def closeEvent(self, event):
        """
        Pencere kapatılırken temizlik yap
        
        Args:
            event: Close event
        """
        # Kaynakları temizle
        self.audio_manager.cleanup()
        
        if self.spotlight:
            self.spotlight.close()
        
        if self.tutorial_widget:
            self.tutorial_widget.close()
        
        event.accept()
