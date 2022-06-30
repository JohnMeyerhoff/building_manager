# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:01:38 2022

@author: john
"""
from typing import Tuple
from wall import Wand

Walls = Tuple[Wand, Wand, Wand, Wand]


class Raum:
    height = 0.0
    name = ""
    number = 0
    walls: Walls = False

    def __init__(self, hoehe, bezeichnung, raumnummer, waende: Walls):
        self.height = hoehe
        self.name = bezeichnung
        self.number = raumnummer
        self.walls = waende

    def print_me(self):
        return f"- Raum (Raumbezeichnung: {self.name}, Raumnummer: {self.number})\n"

    def raumbuch(self):
        unicode_drei = "\u00B3"  # https://www.compart.com/en/unicode/U+00B3
        result = self.print_me()
        indent = " " * 9
        # Dezimaltrennzeichen ist in der Ausgabe ein Punkt.
        result = result + indent + f"Raumvolumen: {self.volume():.2f} m{unicode_drei}\n"
        # Floatformatierung 2 Nachkommastellen

        return result

    def volume(self):
        # berechnet h x l x w wobei von einer rechteckigen form ausgegangen wird.
        return 1.0 * self.walls[0].height * self.walls[0].length * self.walls[1].length
