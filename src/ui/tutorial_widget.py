#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Rehber Gösterim Widget'ı
Ottoman Techs - Teknofest 2026

Rehber adımlarını görsel olarak sunar.
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QProgressBar, QFrame)
from PyQt5.QtCore import Qt, pyqtSignal, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QPixmap, QIcon


class TutorialWidget(QWidget):
    """
    Rehber adımlarını gösteren widget
    """
    
    # Sinyaller
    next_clicked = pyqtSignal()
    previous_clicked = pyqtSignal()
    skip_clicked = pyqtSignal()
    close_clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        """
        Rehber widget'ını başlat
        
        Args:
            parent: Üst widget
        """
        super().__init__(parent)
        
        self.current_step = 0
        self.total_steps = 0
        
        self._setup_ui()
        self._apply_styles()
    
    def _setup_ui(self):
        """
        Kullanıcı arayüzünü oluştur
        """
        # Ana layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Üst kısım - Başlık ve kapat butonu
        header_layout = QHBoxLayout()
        
        self.title_label = QLabel("Rehber Başlığı")
        self.title_label.setObjectName("tutorialTitle")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        
        self.close_button = QPushButton("✕")
        self.close_button.setObjectName("closeButton")
        self.close_button.setFixedSize(40, 40)
        self.close_button.clicked.connect(self.close_clicked.emit)
        
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.close_button)
        
        main_layout.addLayout(header_layout)
        
        # Ayırıcı çizgi
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)
        
        # İçerik alanı
        self.description_label = QLabel("Rehber açıklaması burada görünecek.")
        self.description_label.setObjectName("tutorialDescription")
        self.description_label.setWordWrap(True)
        self.description_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        desc_font = QFont()
        desc_font.setPointSize(12)
        self.description_label.setFont(desc_font)
        
        main_layout.addWidget(self.description_label, 1)
        
        # İlerleme çubuğu
        progress_layout = QVBoxLayout()
        
        self.progress_label = QLabel("Adım 1 / 5")
        self.progress_label.setObjectName("progressLabel")
        self.progress_label.setAlignment(Qt.AlignCenter)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setObjectName("tutorialProgress")
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedHeight(8)
        
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress_bar)
        
        main_layout.addLayout(progress_layout)
        
        # Alt kısım - Butonlar
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.skip_button = QPushButton("Atla")
        self.skip_button.setObjectName("skipButton")
        self.skip_button.setFixedHeight(45)
        self.skip_button.clicked.connect(self.skip_clicked.emit)
        
        button_layout.addWidget(self.skip_button)
        button_layout.addStretch()
        
        self.previous_button = QPushButton("◀ Önceki")
        self.previous_button.setObjectName("previousButton")
        self.previous_button.setFixedHeight(45)
        self.previous_button.setFixedWidth(120)
        self.previous_button.clicked.connect(self.previous_clicked.emit)
        
        self.next_button = QPushButton("Sonraki ▶")
        self.next_button.setObjectName("nextButton")
        self.next_button.setFixedHeight(45)
        self.next_button.setFixedWidth(120)
        self.next_button.clicked.connect(self.next_clicked.emit)
        
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)
        
        main_layout.addLayout(button_layout)
        
        # Widget boyutu
        self.setFixedSize(450, 350)
    
    def _apply_styles(self):
        """
        Widget stillerini uygula - Apple tarzı modern tasarım
        """
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #ffffff, stop:1 #f9f9f9);
                border-radius: 20px;
                border: 1px solid rgba(0, 0, 0, 0.08);
            }
            
            #tutorialTitle {
                color: #1d1d1f;
                padding: 8px;
                font-size: 22pt;
                font-weight: 700;
                letter-spacing: -0.6px;
            }
            
            #tutorialDescription {
                color: #1d1d1f;
                padding: 16px;
                background-color: #f5f5f7;
                border-radius: 12px;
                font-size: 15pt;
                line-height: 1.6;
                letter-spacing: -0.3px;
                border: 1px solid #e8e8ed;
            }
            
            #progressLabel {
                color: #6e6e73;
                font-size: 13pt;
                font-weight: 500;
                margin-bottom: 8px;
                letter-spacing: -0.2px;
            }
            
            #tutorialProgress {
                border: none;
                border-radius: 6px;
                background-color: #e8e8ed;
            }
            
            #tutorialProgress::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #007aff, stop:1 #5ac8fa);
                border-radius: 6px;
            }
            
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #007aff, stop:1 #0051d5);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 12px 24px;
                font-size: 15pt;
                font-weight: 600;
                letter-spacing: -0.3px;
            }
            
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #0077ed, stop:1 #004ec5);
            }
            
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #0051d5, stop:1 #003da8);
                padding: 13px 24px 11px 24px;
            }
            
            QPushButton:disabled {
                background: #d1d1d6;
                color: #8e8e93;
            }
            
            #closeButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #ff3b30, stop:1 #d32f2f);
                font-size: 20pt;
                font-weight: 600;
                border-radius: 20px;
            }
            
            #closeButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #ff2d20, stop:1 #c62828);
            }
            
            #skipButton {
                background: #f5f5f7;
                color: #1d1d1f;
                border: 1px solid #d1d1d6;
            }
            
            #skipButton:hover {
                background: #e8e8ed;
                border: 1px solid #c7c7cc;
            }
            
            #previousButton {
                background: #f5f5f7;
                color: #1d1d1f;
                border: 1px solid #d1d1d6;
            }
            
            #previousButton:hover {
                background: #e8e8ed;
                border: 1px solid #c7c7cc;
            }
            
            #previousButton:disabled {
                background: #f5f5f7;
                color: #c7c7cc;
                border: 1px solid #e8e8ed;
            }
        """)
    
    def set_tutorial_info(self, title: str, description: str, 
                         current_step: int, total_steps: int):
        """
        Rehber bilgilerini güncelle
        
        Args:
            title (str): Adım başlığı
            description (str): Adım açıklaması
            current_step (int): Mevcut adım numarası (1'den başlar)
            total_steps (int): Toplam adım sayısı
        """
        self.title_label.setText(title)
        self.description_label.setText(description)
        self.current_step = current_step
        self.total_steps = total_steps
        
        # İlerleme güncelle
        self.progress_label.setText(f"Adım {current_step} / {total_steps}")
        
        if total_steps > 0:
            progress = int((current_step / total_steps) * 100)
            self.progress_bar.setValue(progress)
        
        # Buton durumlarını güncelle
        self.previous_button.setEnabled(current_step > 1)
        
        # Son adımda "Sonraki" yerine "Bitir" yaz
        if current_step >= total_steps:
            self.next_button.setText("Bitir ✓")
        else:
            self.next_button.setText("Sonraki ▶")
    
    def show_with_animation(self):
        """
        Widget'ı animasyonlu göster
        """
        self.show()
        
        # Fade-in animasyonu
        self.setWindowOpacity(0)
        animation = QPropertyAnimation(self, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.setEasingCurve(QEasingCurve.InOutCubic)
        animation.start()
    
    def hide_with_animation(self):
        """
        Widget'ı animasyonlu gizle
        """
        # Fade-out animasyonu
        animation = QPropertyAnimation(self, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.setEasingCurve(QEasingCurve.InOutCubic)
        animation.finished.connect(self.hide)
        animation.start()
