#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Yol Arkadaşı - Tutorial Manager Test
Ottoman Techs - Teknofest 2026

Rehber yönetim sisteminin test dosyası.
"""

import unittest
import sys
import os

# Proje kök dizinini path'e ekle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.tutorial_manager import TutorialManager, Tutorial, TutorialStep


class TestTutorialManager(unittest.TestCase):
    """
    TutorialManager sınıfı için test senaryoları
    """
    
    def setUp(self):
        """
        Her test öncesi çalışır
        """
        # Test için tutorial manager oluştur
        self.manager = TutorialManager()
    
    def test_load_tutorials(self):
        """
        Rehberlerin yüklendiğini test et
        """
        tutorials = self.manager.get_all_tutorials()
        self.assertGreater(len(tutorials), 0, "En az bir rehber yüklenmeli")
    
    def test_get_tutorial_by_id(self):
        """
        ID ile rehber getirmeyi test et
        """
        tutorial = self.manager.get_tutorial("desktop-basics")
        self.assertIsNotNone(tutorial, "desktop-basics rehberi bulunmalı")
        self.assertEqual(tutorial.id, "desktop-basics")
    
    def test_tutorial_steps(self):
        """
        Rehber adımlarını test et
        """
        tutorial = self.manager.get_tutorial("desktop-basics")
        if tutorial:
            self.assertGreater(len(tutorial.steps), 0, "Rehberde en az bir adım olmalı")
            
            # İlk adımı kontrol et
            first_step = tutorial.get_current_step()
            self.assertIsNotNone(first_step)
            self.assertIsInstance(first_step, TutorialStep)
    
    def test_tutorial_navigation(self):
        """
        Rehber adımları arasında gezinmeyi test et
        """
        tutorial = self.manager.get_tutorial("desktop-basics")
        if tutorial:
            initial_index = tutorial.current_step_index
            
            # İleri git
            result = tutorial.next_step()
            if result:
                self.assertEqual(tutorial.current_step_index, initial_index + 1)
            
            # Geri git
            result = tutorial.previous_step()
            if result:
                self.assertEqual(tutorial.current_step_index, initial_index)
    
    def test_tutorial_progress(self):
        """
        Rehber ilerleme yüzdesini test et
        """
        tutorial = self.manager.get_tutorial("desktop-basics")
        if tutorial:
            progress = tutorial.get_progress()
            self.assertGreaterEqual(progress, 0)
            self.assertLessEqual(progress, 100)
    
    def test_get_categories(self):
        """
        Kategori listesini test et
        """
        categories = self.manager.get_categories()
        self.assertIsInstance(categories, list)
        self.assertGreater(len(categories), 0, "En az bir kategori olmalı")
    
    def test_search_tutorials(self):
        """
        Rehber aramasını test et
        """
        results = self.manager.search_tutorials("masaüstü")
        self.assertIsInstance(results, list)
    
    def test_start_tutorial(self):
        """
        Rehber başlatmayı test et
        """
        result = self.manager.start_tutorial("desktop-basics")
        self.assertTrue(result, "Rehber başlatılmalı")
        
        current = self.manager.get_current_tutorial()
        self.assertIsNotNone(current)
        self.assertEqual(current.id, "desktop-basics")
    
    def test_stop_tutorial(self):
        """
        Rehber durdurmayı test et
        """
        self.manager.start_tutorial("desktop-basics")
        self.manager.stop_tutorial()
        
        current = self.manager.get_current_tutorial()
        self.assertIsNone(current, "Rehber durdurulmalı")


if __name__ == '__main__':
    unittest.main()
