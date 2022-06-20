# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:01:38 2022

@author: john
"""

class Raum:
    height = 0.0
    name = ""
    number = 0
    def __init__(self,hoehe,bezeichnung,raumnummer):
        self.height = hoehe
        self.name = bezeichnung
        self.number = raumnummer
        
    def print_me(self):
        return f"Raum {self.number}: Bezeichnung: {self.name}, Höhe (in m): {self.height}"

    def raumbuch(self):
        result = self.print_me()
        result = result + "\nEnde des Berichts"
        return result