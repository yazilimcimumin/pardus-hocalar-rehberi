#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Yapılandırma Yönetimi
Ottoman Techs - Teknofest 2026

Uygulama ayarlarını yönetir ve kalıcı hale getirir.
"""

import os
import json
from pathlib import Path


class Config:
    """
    Uygulama yapılandırma yöneticisi
    
    Kullanıcı ayarlarını JSON formatında saklar ve yönetir.
    """
    
    # Varsayılan yapılandırma değerleri
    DEFAULT_CONFIG = {
        "first_run": True,
        "version": "1.0.0",
        "language": "tr_TR",
        "autostart": {
            "enabled": True,
            "show_on_boot": True
        },
        "display": {
            "fullscreen_on_start": False,
            "window_width": 1024,
            "window_height": 768,
            "theme": "light"
        },
        "audio": {
            "enabled": True,
            "volume": 80,
            "speed": 1.0
        },
        "tutorials": {
            "completed": [],
            "current": None,
            "show_hints": True
        },
        "accessibility": {
            "high_contrast": False,
            "large_text": False,
            "animation_speed": 1.0
        }
    }
    
    def __init__(self):
        """
        Yapılandırma yöneticisini başlat
        """
        # Yapılandırma dizinini belirle
        self.config_dir = Path.home() / ".config" / "pardus-yol-arkadasi"
        self.config_file = self.config_dir / "config.json"
        
        # Yapılandırma dizinini oluştur
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Yapılandırmayı yükle
        self.config = self._load_config()
    
    def _load_config(self):
        """
        Yapılandırma dosyasını yükle
        
        Returns:
            dict: Yapılandırma sözlüğü
        """
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    loaded_config = json.load(f)
                
                # Varsayılan değerlerle birleştir (yeni anahtarlar için)
                config = self.DEFAULT_CONFIG.copy()
                self._deep_update(config, loaded_config)
                
                return config
            except (json.JSONDecodeError, IOError) as e:
                print(f"[UYARI] Yapılandırma dosyası okunamadı: {e}")
                return self.DEFAULT_CONFIG.copy()
        else:
            # İlk çalıştırma - varsayılan yapılandırmayı kullan
            return self.DEFAULT_CONFIG.copy()
    
    def _deep_update(self, base_dict, update_dict):
        """
        İç içe sözlükleri derin güncelleme
        
        Args:
            base_dict (dict): Temel sözlük
            update_dict (dict): Güncellenecek değerler
        """
        for key, value in update_dict.items():
            if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
                self._deep_update(base_dict[key], value)
            else:
                base_dict[key] = value
    
    def save(self):
        """
        Yapılandırmayı dosyaya kaydet
        
        Returns:
            bool: Başarılı ise True, değilse False
        """
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"[HATA] Yapılandırma dosyası kaydedilemedi: {e}")
            return False
    
    def get(self, key, default=None):
        """
        Yapılandırma değerini al
        
        Args:
            key (str): Nokta notasyonuyla anahtar (örn: "audio.volume")
            default: Anahtar bulunamazsa döndürülecek değer
        
        Returns:
            Yapılandırma değeri veya varsayılan değer
        """
        keys = key.split(".")
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """
        Yapılandırma değerini ayarla
        
        Args:
            key (str): Nokta notasyonuyla anahtar (örn: "audio.volume")
            value: Ayarlanacak değer
        """
        keys = key.split(".")
        config = self.config
        
        # Son anahtara kadar ilerle
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # Değeri ayarla
        config[keys[-1]] = value
    
    def is_first_run(self):
        """
        İlk çalıştırma kontrolü
        
        Returns:
            bool: İlk çalıştırma ise True
        """
        return self.get("first_run", True)
    
    def mark_tutorial_completed(self, tutorial_id):
        """
        Bir rehberi tamamlandı olarak işaretle
        
        Args:
            tutorial_id (str): Rehber kimliği
        """
        completed = self.get("tutorials.completed", [])
        if tutorial_id not in completed:
            completed.append(tutorial_id)
            self.set("tutorials.completed", completed)
            self.save()
    
    def is_tutorial_completed(self, tutorial_id):
        """
        Rehberin tamamlanıp tamamlanmadığını kontrol et
        
        Args:
            tutorial_id (str): Rehber kimliği
        
        Returns:
            bool: Tamamlandıysa True
        """
        completed = self.get("tutorials.completed", [])
        return tutorial_id in completed
    
    def reset(self):
        """
        Yapılandırmayı varsayılan değerlere sıfırla
        """
        self.config = self.DEFAULT_CONFIG.copy()
        self.save()
    
    def export_config(self, file_path):
        """
        Yapılandırmayı dışa aktar
        
        Args:
            file_path (str): Dışa aktarılacak dosya yolu
        
        Returns:
            bool: Başarılı ise True
        """
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"[HATA] Yapılandırma dışa aktarılamadı: {e}")
            return False
    
    def import_config(self, file_path):
        """
        Yapılandırmayı içe aktar
        
        Args:
            file_path (str): İçe aktarılacak dosya yolu
        
        Returns:
            bool: Başarılı ise True
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                imported_config = json.load(f)
            
            self._deep_update(self.config, imported_config)
            self.save()
            return True
        except (json.JSONDecodeError, IOError) as e:
            print(f"[HATA] Yapılandırma içe aktarılamadı: {e}")
            return False
