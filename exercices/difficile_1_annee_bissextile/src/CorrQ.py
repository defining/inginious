#!/usr/bin/python3
# -*- coding: utf-8 -*-

def verifier_bissextile():
    """
    Détermine si une année est bissextile
    """
    annee = int(input("Entrez une annee: "))
    
    if (annee % 4) == 0:
        if (annee % 100) != 0:
            print(str(annee) + " est une annee bissextile")
        elif (annee % 400) == 0:
            print(str(annee) + " est une annee bissextile")
        else:
            print(str(annee) + " n'est pas une annee bissextile")
    else:
        print(str(annee) + " n'est pas une annee bissextile")
