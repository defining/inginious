#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import CorrQ as corr
import q

class TestVerifierMajorite(unittest.TestCase):
    
    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(hasattr(q, 'verifier_majorite'), 
                       "La fonction 'verifier_majorite' n'existe pas.")
    
    @patch('builtins.input', side_effect=['17'])
    def test_mineur(self, mock_input):
        """Test avec une personne mineure"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.verifier_majorite()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.verifier_majorite()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour un mineur.\nAttendu:\n{expected}\nObtenu:\n{actual}")
    
    @patch('builtins.input', side_effect=['18'])
    def test_exactement_18(self, mock_input):
        """Test avec exactement 18 ans"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.verifier_majorite()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.verifier_majorite()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour 18 ans pile.")
    
    @patch('builtins.input', side_effect=['25'])
    def test_majeur(self, mock_input):
        """Test avec une personne majeure"""
        captured_corr = io.StringIO()
        sys.stdout = captured_corr
        corr.verifier_majorite()
        sys.stdout = sys.__stdout__
        expected = captured_corr.getvalue()
        
        captured_stu = io.StringIO()
        sys.stdout = captured_stu
        q.verifier_majorite()
        sys.stdout = sys.__stdout__
        actual = captured_stu.getvalue()
        
        self.assertEqual(actual, expected,
                        f"Sortie incorrecte pour un majeur.")

if __name__ == '__main__':
    unittest.main()
