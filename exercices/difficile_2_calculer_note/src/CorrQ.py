#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calculer_note():
    """
    Calcule la note finale d'un étudiant et détermine le résultat
    """
    examen = float(input("Entrez la note de l'examen: "))
    projet = float(input("Entrez la note du projet: "))
    
    note_finale = examen * 0.6 + projet * 0.4
    print("Note finale: " + str(note_finale))
    
    if note_finale < 10:
        print("Echec")
    elif note_finale < 12:
        print("Reussite")
    elif note_finale < 14:
        print("Satisfaction")
    elif note_finale < 16:
        print("Distinction")
    else:
        print("Grande distinction")
