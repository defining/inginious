#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestConvertirTemperature(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'convertir_temperature'), 
                       "La fonction 'convertir_temperature' n'existe pas.")
    
    @patch('builtins.input', side_effect=['25.0'])
    def test_cas1(self, mock_input):
        """Test avec 25°C"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.convertir_temperature()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.convertir_temperature()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte.\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['0'])
    def test_cas2(self, mock_input):
        """Test avec 0°C"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.convertir_temperature()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.convertir_temperature()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour 0°C.")

if __name__ == '__main__':
    unittest.main()
