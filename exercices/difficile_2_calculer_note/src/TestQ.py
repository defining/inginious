#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestCalculerNote(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'calculer_note'), 
                       "La fonction 'calculer_note' n'existe pas.")
    
    @patch('builtins.input', side_effect=['15.0', '14.0'])
    def test_distinction(self, mock_input):
        """Test avec distinction"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_note()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_note()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte.\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['8.0', '12.0'])
    def test_echec(self, mock_input):
        """Test avec échec"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_note()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_note()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour échec.")
    
    @patch('builtins.input', side_effect=['18.0', '17.0'])
    def test_grande_distinction(self, mock_input):
        """Test avec grande distinction"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.calculer_note()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.calculer_note()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour grande distinction.")

if __name__ == '__main__':
    unittest.main()
