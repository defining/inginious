#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestAfficherInfo(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'afficher_info'), 
                       "La fonction 'afficher_info' n'existe pas.")
    
    @patch('builtins.input', side_effect=['Alice', '20'])
    def test_cas1(self, mock_input):
        """Test avec Alice, 20 ans"""
        # Capturer la sortie de la fonction correcte
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.afficher_info()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        # Capturer la sortie de l'étudiant
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.afficher_info()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte.\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['Bob', '25'])
    def test_cas2(self, mock_input):
        """Test avec Bob, 25 ans"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.afficher_info()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.afficher_info()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte avec d'autres valeurs.")

if __name__ == '__main__':
    unittest.main()
