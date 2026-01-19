#!/usr/bin/python3
# -*- coding: utf-8 -*-

def afficher_info():
    """
    Demande le prénom et l'âge de l'utilisateur et affiche ces informations
    """
    prenom = input("Entrez votre prenom: ")
    age = int(input("Entrez votre age: "))
    print("Bonjour " + prenom + ", vous avez " + str(age) + " ans.")
