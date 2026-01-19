#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calculer_parking():
    """
    Calcule le tarif de parking selon le type de véhicule et la durée
    """
    type_vehicule = input("Type de vehicule (voiture/moto): ")
    heures = int(input("Nombre d'heures: "))
    
    if type_vehicule == "voiture":
        if heures == 1:
            tarif = 3.0
        elif heures <= 5:
            tarif = 3.0 + (heures - 1) * 2.0
        else:
            tarif = 3.0 + 4 * 2.0 + (heures - 5) * 1.5
    else:  # moto
        if heures == 1:
            tarif = 2.0
        elif heures <= 5:
            tarif = 2.0 + (heures - 1) * 1.5
        else:
            tarif = 2.0 + 4 * 1.5 + (heures - 5) * 1.0
    
    print("Tarif: " + str(tarif) + " euros")
