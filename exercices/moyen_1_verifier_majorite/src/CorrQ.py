#!/usr/bin/python3
# -*- coding: utf-8 -*-

def verifier_majorite():
    """
    Vérifie si une personne est majeure ou mineure
    """
    age = int(input("Entrez votre age: "))
    
    if age < 18:
        print("Vous etes mineur")
    elif age == 18:
        print("Vous venez de devenir majeur")
    else:
        print("Vous etes majeur")
