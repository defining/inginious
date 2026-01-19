#!/usr/bin/python3
# -*- coding: utf-8 -*-

def convertir_temperature():
    """
    Convertit une température de Celsius en Fahrenheit
    """
    celsius = float(input("Entrez la temperature en Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(str(celsius) + " degrees Celsius = " + str(fahrenheit) + " degrees Fahrenheit")
