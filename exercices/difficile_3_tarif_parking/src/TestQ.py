#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestCalculerParking(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'calculer_parking'), 
                       "La fonction 'calculer_parking' n'existe pas.")
    
    @patch('builtins.input', side_effect=['voiture', '3'])
    def test_voiture_3h(self, mock_input):
        """Test voiture 3 heures"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_parking()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_parking()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte.\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['moto', '7'])
    def test_moto_7h(self, mock_input):
        """Test moto 7 heures"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_parking()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_parking()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour moto 7h.")
    
    @patch('builtins.input', side_effect=['voiture', '1'])
    def test_voiture_1h(self, mock_input):
        """Test voiture 1 heure"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_parking()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_parking()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour voiture 1h.")

if __name__ == '__main__':
    unittest.main()
