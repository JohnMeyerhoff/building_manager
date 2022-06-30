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
        return f"- Raum (Raumbezeichnung: {self.name}, Raumnummer: {self.number}:  \n"

    def raumbuch(self):
        result = self.print_me()
        result = result + "\n"+Raum.line(60)
        result = result + f"\nVolumen des Raums: {self.volume()}"
        result = result + "\nEnde des Berichts"
        return result

    def volume(self):
        # berechnet h x l x w wobei von einer rechteckigen form ausgegangen wird.
        return self.walls[0].height * self.walls[0].length * self.walls[1].length

    @staticmethod
    def line(len: int):
        return "-"*len
