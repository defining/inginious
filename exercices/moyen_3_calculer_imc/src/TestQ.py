#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestCalculerIMC(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'calculer_imc'), 
                       "La fonction 'calculer_imc' n'existe pas.")
    
    @patch('builtins.input', side_effect=['70.0', '1.75'])
    def test_normal(self, mock_input):
        """Test IMC normal"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_imc()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_imc()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte.\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['50.0', '1.70'])
    def test_insuffisance(self, mock_input):
        """Test insuffisance pondérale"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_imc()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_imc()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour insuffisance pondérale.")
    
    @patch('builtins.input', side_effect=['90.0', '1.70'])
    def test_obesite(self, mock_input):
        """Test obésité"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_imc()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_imc()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour obésité.")

if __name__ == '__main__':
    unittest.main()
