#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calculer_imc():
    """
    Calcule l'IMC et donne une interprétation
    """
    poids = float(input("Entrez votre poids en kg: "))
    taille = float(input("Entrez votre taille en m: "))
    
    imc = poids / (taille * taille)
    print("Votre IMC est: " + str(imc))
    
    if imc < 18.5:
        print("Insuffisance ponderale")
    elif imc < 25:
        print("Corpulence normale")
    elif imc < 30:
        print("Surpoids")
    else:
        print("Obesite")
