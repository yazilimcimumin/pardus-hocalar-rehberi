#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Ses Yönetim Sistemi
Ottoman Techs - Teknofest 2026

Rehber sesli anlatımlarını yönetir ve oynatır.
"""

import os
from pathlib import Path
from typing import Optional
from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class AudioManager(QObject):
    """
    Ses dosyalarını yönetir ve oynatır
    """
    
    # Sinyaller
    playback_started = pyqtSignal()
    playback_finished = pyqtSignal()
    playback_error = pyqtSignal(str)
    position_changed = pyqtSignal(int)  # Milisaniye cinsinden pozisyon
    
    def __init__(self, audio_dir: Optional[str] = None):
        """
        Ses yöneticisini başlat
        
        Args:
            audio_dir (str, optional): Ses dosyalarının bulunduğu dizin
        """
        super().__init__()
        
        if audio_dir is None:
            # Varsayılan ses dizini
            self.audio_dir = Path(__file__).parent.parent / "data" / "audio"
        else:
            self.audio_dir = Path(audio_dir)
        
        # Ses dizinini oluştur (yoksa)
        self.audio_dir.mkdir(parents=True, exist_ok=True)
        
        # Media player oluştur
        self.player = QMediaPlayer()
        
        # Sinyalleri bağla
        self.player.stateChanged.connect(self._on_state_changed)
        self.player.error.connect(self._on_error)
        self.player.positionChanged.connect(self._on_position_changed)
        
        # Ses ayarları
        self.volume = 80  # 0-100 arası
        self.playback_rate = 1.0  # Oynatma hızı
        self.is_muted = False
        
        self._apply_settings()
    
    def _apply_settings(self):
        """
        Ses ayarlarını uygula
        """
        self.player.setVolume(self.volume)
        self.player.setPlaybackRate(self.playback_rate)
        self.player.setMuted(self.is_muted)
    
    def _on_state_changed(self, state):
        """
        Oynatıcı durumu değiştiğinde çağrılır
        
        Args:
            state: QMediaPlayer durumu
        """
        if state == QMediaPlayer.PlayingState:
            self.playback_started.emit()
        elif state == QMediaPlayer.StoppedState:
            self.playback_finished.emit()
    
    def _on_error(self, error):
        """
        Hata oluştuğunda çağrılır
        
        Args:
            error: QMediaPlayer hatası
        """
        error_message = self.player.errorString()
        print(f"[HATA] Ses oynatma hatası: {error_message}")
        self.playback_error.emit(error_message)
    
    def _on_position_changed(self, position):
        """
        Oynatma pozisyonu değiştiğinde çağrılır
        
        Args:
            position (int): Milisaniye cinsinden pozisyon
        """
        self.position_changed.emit(position)
    
    def play(self, audio_file: str) -> bool:
        """
        Ses dosyasını oynat
        
        Args:
            audio_file (str): Ses dosyası adı veya yolu
        
        Returns:
            bool: Başarılı ise True
        """
        # Dosya yolunu belirle
        if os.path.isabs(audio_file):
            audio_path = Path(audio_file)
        else:
            audio_path = self.audio_dir / audio_file
        
        # Dosya kontrolü
        if not audio_path.exists():
            error_msg = f"Ses dosyası bulunamadı: {audio_path}"
            print(f"[HATA] {error_msg}")
            self.playback_error.emit(error_msg)
            return False
        
        # Medya içeriğini ayarla ve oynat
        try:
            url = QUrl.fromLocalFile(str(audio_path))
            content = QMediaContent(url)
            self.player.setMedia(content)
            self.player.play()
            return True
        except Exception as e:
            error_msg = f"Ses oynatma hatası: {e}"
            print(f"[HATA] {error_msg}")
            self.playback_error.emit(error_msg)
            return False
    
    def stop(self):
        """
        Oynatmayı durdur
        """
        self.player.stop()
    
    def pause(self):
        """
        Oynatmayı duraklat
        """
        self.player.pause()
    
    def resume(self):
        """
        Duraklatılmış oynatmayı devam ettir
        """
        if self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
    
    def set_volume(self, volume: int):
        """
        Ses seviyesini ayarla
        
        Args:
            volume (int): 0-100 arası ses seviyesi
        """
        self.volume = max(0, min(100, volume))
        self.player.setVolume(self.volume)
    
    def get_volume(self) -> int:
        """
        Mevcut ses seviyesini al
        
        Returns:
            int: 0-100 arası ses seviyesi
        """
        return self.volume
    
    def set_playback_rate(self, rate: float):
        """
        Oynatma hızını ayarla
        
        Args:
            rate (float): Oynatma hızı (0.5 = yarı hız, 1.0 = normal, 2.0 = iki kat hız)
        """
        self.playback_rate = max(0.5, min(2.0, rate))
        self.player.setPlaybackRate(self.playback_rate)
    
    def get_playback_rate(self) -> float:
        """
        Mevcut oynatma hızını al
        
        Returns:
            float: Oynatma hızı
        """
        return self.playback_rate
    
    def mute(self):
        """
        Sesi kapat
        """
        self.is_muted = True
        self.player.setMuted(True)
    
    def unmute(self):
        """
        Sesi aç
        """
        self.is_muted = False
        self.player.setMuted(False)
    
    def toggle_mute(self):
        """
        Sesi aç/kapat
        """
        if self.is_muted:
            self.unmute()
        else:
            self.mute()
    
    def is_playing(self) -> bool:
        """
        Oynatma devam ediyor mu?
        
        Returns:
            bool: Oynatılıyorsa True
        """
        return self.player.state() == QMediaPlayer.PlayingState
    
    def get_duration(self) -> int:
        """
        Mevcut ses dosyasının toplam süresini al
        
        Returns:
            int: Milisaniye cinsinden süre
        """
        return self.player.duration()
    
    def get_position(self) -> int:
        """
        Mevcut oynatma pozisyonunu al
        
        Returns:
            int: Milisaniye cinsinden pozisyon
        """
        return self.player.position()
    
    def seek(self, position: int):
        """
        Belirli bir pozisyona atla
        
        Args:
            position (int): Milisaniye cinsinden pozisyon
        """
        self.player.setPosition(position)
    
    def cleanup(self):
        """
        Kaynakları temizle
        """
        self.stop()
        self.player.setMedia(QMediaContent())
