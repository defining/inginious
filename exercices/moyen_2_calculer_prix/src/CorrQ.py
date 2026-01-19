#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calculer_prix():
    """
    Calcule le prix final avec réductions selon le prix initial
    """
    prix = float(input("Entrez le prix initial: "))
    
    if prix < 50:
        prix_final = prix
    elif prix <= 100:
        prix_final = prix * 0.9  # Réduction de 10%
    else:
        prix_final = prix * 0.8  # Réduction de 20%
    
    print("Prix final: " + str(prix_final) + " euros")
