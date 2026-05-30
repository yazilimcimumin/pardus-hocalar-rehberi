#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Spotlight Efekt Widget'ı
Ottoman Techs - Teknofest 2026

Ekrandaki belirli bir alanı vurgulayan spotlight efekti sağlar.
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QRect, QPoint, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt5.QtGui import QPainter, QColor, QPainterPath, QRegion


class SpotlightWidget(QWidget):
    """
    Ekranın belirli bir bölgesini vurgulayan spotlight widget'ı
    
    Ekranın geri kalanını karartarak, belirli bir alanı öne çıkarır.
    """
    
    def __init__(self, parent=None):
        """
        Spotlight widget'ını başlat
        
        Args:
            parent: Üst widget
        """
        super().__init__(parent)
        
        # Widget ayarları
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        # Spotlight özellikleri
        self._spotlight_rect = QRect(0, 0, 0, 0)
        self._spotlight_radius = 10
        self._overlay_opacity = 0.7
        self._spotlight_padding = 20
        
        # Animasyon
        self._animation = QPropertyAnimation(self, b"spotlightRect")
        self._animation.setDuration(500)
        self._animation.setEasingCurve(QEasingCurve.InOutCubic)
        
        # Renkler
        self.overlay_color = QColor(0, 0, 0, int(255 * self._overlay_opacity))
        self.spotlight_border_color = QColor(52, 152, 219, 200)  # Mavi vurgu
        self.spotlight_border_width = 3
        
        # Başlangıçta gizli
        self.hide()
    
    @pyqtProperty(QRect)
    def spotlightRect(self):
        """
        Spotlight dikdörtgenini al (animasyon için)
        
        Returns:
            QRect: Spotlight dikdörtgeni
        """
        return self._spotlight_rect
    
    @spotlightRect.setter
    def spotlightRect(self, rect):
        """
        Spotlight dikdörtgenini ayarla (animasyon için)
        
        Args:
            rect (QRect): Yeni spotlight dikdörtgeni
        """
        self._spotlight_rect = rect
        self.update()
    
    def set_spotlight_target(self, rect: QRect, animated: bool = True):
        """
        Spotlight hedefini ayarla
        
        Args:
            rect (QRect): Vurgulanacak alan
            animated (bool): Animasyonlu geçiş yapılsın mı?
        """
        # Padding ekle
        padded_rect = rect.adjusted(
            -self._spotlight_padding,
            -self._spotlight_padding,
            self._spotlight_padding,
            self._spotlight_padding
        )
        
        if animated:
            # Animasyonlu geçiş
            self._animation.stop()
            self._animation.setStartValue(self._spotlight_rect)
            self._animation.setEndValue(padded_rect)
            self._animation.start()
        else:
            # Anında geçiş
            self._spotlight_rect = padded_rect
            self.update()
    
    def set_spotlight_radius(self, radius: int):
        """
        Spotlight köşe yuvarlaklığını ayarla
        
        Args:
            radius (int): Köşe yarıçapı (piksel)
        """
        self._spotlight_radius = radius
        self.update()
    
    def set_overlay_opacity(self, opacity: float):
        """
        Overlay opaklığını ayarla
        
        Args:
            opacity (float): 0.0 (şeffaf) - 1.0 (opak) arası
        """
        self._overlay_opacity = max(0.0, min(1.0, opacity))
        self.overlay_color.setAlpha(int(255 * self._overlay_opacity))
        self.update()
    
    def set_spotlight_padding(self, padding: int):
        """
        Spotlight padding'ini ayarla
        
        Args:
            padding (int): Padding miktarı (piksel)
        """
        self._spotlight_padding = padding
    
    def show_spotlight(self):
        """
        Spotlight'ı göster
        """
        self.show()
        self.raise_()
    
    def hide_spotlight(self):
        """
        Spotlight'ı gizle
        """
        self.hide()
    
    def paintEvent(self, event):
        """
        Widget'ı çiz
        
        Args:
            event: Paint event
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Tüm ekranı karart
        painter.fillRect(self.rect(), self.overlay_color)
        
        # Spotlight alanını temizle (şeffaf yap)
        if not self._spotlight_rect.isEmpty():
            # Spotlight path oluştur
            spotlight_path = QPainterPath()
            spotlight_path.addRoundedRect(
                self._spotlight_rect.x(),
                self._spotlight_rect.y(),
                self._spotlight_rect.width(),
                self._spotlight_rect.height(),
                self._spotlight_radius,
                self._spotlight_radius
            )
            
            # Spotlight alanını temizle
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillPath(spotlight_path, Qt.transparent)
            
            # Spotlight kenarlığını çiz
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            painter.setPen(Qt.NoPen)
            painter.setBrush(Qt.NoBrush)
            
            # Kenarlık için pen ayarla
            from PyQt5.QtGui import QPen
            pen = QPen(self.spotlight_border_color, self.spotlight_border_width)
            painter.setPen(pen)
            painter.drawRoundedRect(
                self._spotlight_rect,
                self._spotlight_radius,
                self._spotlight_radius
            )
    
    def resizeEvent(self, event):
        """
        Widget yeniden boyutlandırıldığında
        
        Args:
            event: Resize event
        """
        super().resizeEvent(event)
        self.update()
    
    def mousePressEvent(self, event):
        """
        Fare tıklaması - spotlight dışındaki tıklamaları engelle
        
        Args:
            event: Mouse event
        """
        # Spotlight içindeki tıklamalara izin ver
        if self._spotlight_rect.contains(event.pos()):
            event.ignore()
        else:
            event.accept()
