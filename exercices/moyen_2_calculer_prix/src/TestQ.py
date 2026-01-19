#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestCalculerPrix(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'calculer_prix'), 
                       "La fonction 'calculer_prix' n'existe pas.")
    
    @patch('builtins.input', side_effect=['30.0'])
    def test_sans_reduction(self, mock_input):
        """Test sans réduction (< 50)"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_prix()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_prix()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour prix < 50.\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['80.0'])
    def test_reduction_10(self, mock_input):
        """Test avec réduction de 10% (50-100)"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_prix()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_prix()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour prix entre 50 et 100.")
    
    @patch('builtins.input', side_effect=['150.0'])
    def test_reduction_20(self, mock_input):
        """Test avec réduction de 20% (> 100)"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_prix()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_prix()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour prix > 100.")

if __name__ == '__main__':
    unittest.main()
