#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Rehber Yönetim Sistemi
Ottoman Techs - Teknofest 2026

Rehber içeriklerini yükler, yönetir ve sırayla sunar.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Optional


class TutorialStep:
    """
    Tek bir rehber adımını temsil eder
    """
    
    def __init__(self, data: dict):
        """
        Rehber adımını başlat
        
        Args:
            data (dict): Adım verileri
        """
        self.title = data.get("title", "")
        self.description = data.get("description", "")
        self.target = data.get("target", None)  # CSS selector veya koordinat
        self.target_type = data.get("target_type", "selector")  # selector, coordinate, window
        self.audio_file = data.get("audio", None)
        self.duration = data.get("duration", 5)  # Saniye cinsinden
        self.action = data.get("action", None)  # Kullanıcıdan beklenen aksiyon
        self.highlight_area = data.get("highlight_area", None)  # Vurgulanacak alan
        self.animation = data.get("animation", "fade")  # Animasyon tipi
    
    def __repr__(self):
        return f"<TutorialStep: {self.title}>"


class Tutorial:
    """
    Tam bir rehber modülünü temsil eder
    """
    
    def __init__(self, data: dict):
        """
        Rehberi başlat
        
        Args:
            data (dict): Rehber verileri
        """
        self.id = data.get("id", "")
        self.title = data.get("title", "")
        self.description = data.get("description", "")
        self.category = data.get("category", "general")
        self.difficulty = data.get("difficulty", "beginner")  # beginner, intermediate, advanced
        self.estimated_time = data.get("estimated_time", 5)  # Dakika cinsinden
        self.icon = data.get("icon", "default")
        self.prerequisites = data.get("prerequisites", [])  # Önkoşul rehberler
        
        # Adımları yükle
        self.steps = [TutorialStep(step) for step in data.get("steps", [])]
        
        self.current_step_index = 0
    
    def get_current_step(self) -> Optional[TutorialStep]:
        """
        Mevcut adımı al
        
        Returns:
            TutorialStep veya None
        """
        if 0 <= self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]
        return None
    
    def next_step(self) -> bool:
        """
        Sonraki adıma geç
        
        Returns:
            bool: Sonraki adım varsa True
        """
        if self.current_step_index < len(self.steps) - 1:
            self.current_step_index += 1
            return True
        return False
    
    def previous_step(self) -> bool:
        """
        Önceki adıma geç
        
        Returns:
            bool: Önceki adım varsa True
        """
        if self.current_step_index > 0:
            self.current_step_index -= 1
            return True
        return False
    
    def reset(self):
        """
        Rehberi başa al
        """
        self.current_step_index = 0
    
    def is_completed(self) -> bool:
        """
        Rehber tamamlandı mı?
        
        Returns:
            bool: Tamamlandıysa True
        """
        return self.current_step_index >= len(self.steps)
    
    def get_progress(self) -> float:
        """
        Rehber ilerleme yüzdesini al
        
        Returns:
            float: 0-100 arası ilerleme yüzdesi
        """
        if len(self.steps) == 0:
            return 100.0
        return (self.current_step_index / len(self.steps)) * 100
    
    def __repr__(self):
        return f"<Tutorial: {self.title} ({len(self.steps)} adım)>"


class TutorialManager:
    """
    Tüm rehberleri yönetir
    """
    
    def __init__(self, tutorials_dir: Optional[str] = None):
        """
        Rehber yöneticisini başlat
        
        Args:
            tutorials_dir (str, optional): Rehber dosyalarının bulunduğu dizin
        """
        if tutorials_dir is None:
            # Varsayılan rehber dizini
            self.tutorials_dir = Path(__file__).parent.parent / "data" / "tutorials"
        else:
            self.tutorials_dir = Path(tutorials_dir)
        
        self.tutorials: Dict[str, Tutorial] = {}
        self.current_tutorial: Optional[Tutorial] = None
        
        # Rehberleri yükle
        self._load_tutorials()
    
    def _load_tutorials(self):
        """
        Tüm rehber dosyalarını yükle
        """
        if not self.tutorials_dir.exists():
            print(f"[UYARI] Rehber dizini bulunamadı: {self.tutorials_dir}")
            return
        
        # JSON dosyalarını tara
        for json_file in self.tutorials_dir.glob("*.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                tutorial = Tutorial(data)
                self.tutorials[tutorial.id] = tutorial
                
                print(f"[BİLGİ] Rehber yüklendi: {tutorial.title}")
            
            except (json.JSONDecodeError, IOError) as e:
                print(f"[HATA] Rehber yüklenemedi ({json_file}): {e}")
    
    def get_tutorial(self, tutorial_id: str) -> Optional[Tutorial]:
        """
        Belirli bir rehberi al
        
        Args:
            tutorial_id (str): Rehber kimliği
        
        Returns:
            Tutorial veya None
        """
        return self.tutorials.get(tutorial_id)
    
    def get_all_tutorials(self) -> List[Tutorial]:
        """
        Tüm rehberleri al
        
        Returns:
            List[Tutorial]: Rehber listesi
        """
        return list(self.tutorials.values())
    
    def get_tutorials_by_category(self, category: str) -> List[Tutorial]:
        """
        Kategoriye göre rehberleri filtrele
        
        Args:
            category (str): Kategori adı
        
        Returns:
            List[Tutorial]: Filtrelenmiş rehber listesi
        """
        return [t for t in self.tutorials.values() if t.category == category]
    
    def get_tutorials_by_difficulty(self, difficulty: str) -> List[Tutorial]:
        """
        Zorluk seviyesine göre rehberleri filtrele
        
        Args:
            difficulty (str): Zorluk seviyesi (beginner, intermediate, advanced)
        
        Returns:
            List[Tutorial]: Filtrelenmiş rehber listesi
        """
        return [t for t in self.tutorials.values() if t.difficulty == difficulty]
    
    def start_tutorial(self, tutorial_id: str) -> bool:
        """
        Bir rehberi başlat
        
        Args:
            tutorial_id (str): Rehber kimliği
        
        Returns:
            bool: Başarılı ise True
        """
        tutorial = self.get_tutorial(tutorial_id)
        if tutorial:
            tutorial.reset()
            self.current_tutorial = tutorial
            return True
        return False
    
    def get_current_tutorial(self) -> Optional[Tutorial]:
        """
        Mevcut aktif rehberi al
        
        Returns:
            Tutorial veya None
        """
        return self.current_tutorial
    
    def stop_tutorial(self):
        """
        Mevcut rehberi durdur
        """
        self.current_tutorial = None
    
    def get_categories(self) -> List[str]:
        """
        Tüm rehber kategorilerini al
        
        Returns:
            List[str]: Kategori listesi
        """
        categories = set()
        for tutorial in self.tutorials.values():
            categories.add(tutorial.category)
        return sorted(list(categories))
    
    def search_tutorials(self, query: str) -> List[Tutorial]:
        """
        Rehberlerde arama yap
        
        Args:
            query (str): Arama sorgusu
        
        Returns:
            List[Tutorial]: Eşleşen rehberler
        """
        query = query.lower()
        results = []
        
        for tutorial in self.tutorials.values():
            # Başlık ve açıklamada ara
            if (query in tutorial.title.lower() or 
                query in tutorial.description.lower()):
                results.append(tutorial)
        
        return results
    
    def reload_tutorials(self):
        """
        Rehberleri yeniden yükle
        """
        self.tutorials.clear()
        self.current_tutorial = None
        self._load_tutorials()
