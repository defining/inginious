#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calculer_rectangle():
    """
    Demande les dimensions d'un rectangle et calcule sa surface
    """
    largeur = float(input("Entrez la largeur: "))
    hauteur = float(input("Entrez la hauteur: "))
    surface = largeur * hauteur
    print("La surface du rectangle est " + str(surface))
