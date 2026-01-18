#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from unittest.mock import patch
import q   # module étudiant

class TestCalculerRectangle(unittest.TestCase):

    def test_exist(self):
        """Vérifie que la fonction existe"""
        self.assertTrue(
            hasattr(q, 'calculer_rectangle'),
            "La fonction 'calculer_rectangle' n'existe pas."
        )

    @patch('builtins.input', side_effect=['5.5', '3.0'])
    def test_cas1(self, mock_input):
        """Test avec 5.5 x 3.0"""
        captured = io.StringIO()
        sys.stdout = captured

        q.calculer_rectangle()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "16.5\n")

    @patch('builtins.input', side_effect=['10', '4.5'])
    def test_cas2(self, mock_input):
        """Test avec 10 x 4.5"""
        captured = io.StringIO()
        sys.stdout = captured

        q.calculer_rectangle()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "45.0\n")

if __name__ == '__main__':
    unittest.main()
