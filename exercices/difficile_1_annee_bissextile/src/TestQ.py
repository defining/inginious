#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestVerifierBissextile(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'verifier_bissextile'), 
                       "La fonction 'verifier_bissextile' n'existe pas.")
    
    @patch('builtins.input', side_effect=['2000'])
    def test_2000(self, mock_input):
        """Test 2000 (bissextile, divisible par 400)"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.verifier_bissextile()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.verifier_bissextile()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Erreur pour 2000 (devrait être bissextile).\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['1900'])
    def test_1900(self, mock_input):
        """Test 1900 (pas bissextile, divisible par 100 mais pas 400)"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.verifier_bissextile()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.verifier_bissextile()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Erreur pour 1900 (ne devrait pas être bissextile).")
    
    @patch('builtins.input', side_effect=['2024'])
    def test_2024(self, mock_input):
        """Test 2024 (bissextile, divisible par 4 mais pas 100)"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.verifier_bissextile()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.verifier_bissextile()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Erreur pour 2024 (devrait être bissextile).")
    
    @patch('builtins.input', side_effect=['2023'])
    def test_2023(self, mock_input):
        """Test 2023 (pas bissextile, pas divisible par 4)"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.verifier_bissextile()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.verifier_bissextile()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Erreur pour 2023 (ne devrait pas être bissextile).")

if __name__ == '__main__':
    unittest.main()
