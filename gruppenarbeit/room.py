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
        unicode_zwei = "\u00B2"
        result = self.print_me()
        indent = " " * 9
        # Dezimaltrennzeichen ist in der Ausgabe ein Punkt.
        result = result + indent + f"Raumvolumen: {self.volume():.2f} m{unicode_drei}\n"
        result = result + indent + f"Raumumfang: {self.circumference():.2f} m\n"
        result = result + "\n" + indent + f"Raumseitenflaeche Brutto: {self.total_wall_area():.2f} m\n"
        result = result + "\n" + indent + f"Raumseitenflaeche Netto: {self.vob_wall_area():.2f} m\n"
        # Floatformatierung 2 Nachkommastellen

        return result

    def volume(self):
        # berechnet h x l x w wobei von einer rechteckigen form ausgegangen wird.
        return 1.0 * self.walls[0].height * self.walls[0].length * self.walls[1].length

    def circumference(self):
        # berechnet l x w wobei von einer rechteckigen form ausgegangen wird.
        return 1.0 * self.walls[0].length * self.walls[1].length

    def total_wall_area(self):
        return self.walls[0].wall_area() + self.walls[1].wall_area() + self.walls[2].wall_area() + self.walls[
            3].wall_area()

    def vob_wall_area(self):
        return self.walls[0].vob_wall_area() + self.walls[1].vob_wall_area() + self.walls[2].vob_wall_area() + \
               self.walls[3].vob_wall_area()
