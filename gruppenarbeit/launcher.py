# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:58:01 2022

@author: john
"""
from room import Raum
from wall import Wand


class Launcher:
    
    @staticmethod
    def run():
        # annotation aus SonarLint  (python:S5719)
        w1 = Wand(5, 4, 0.2)
        w2 = Wand(5, 4, 0.2)
        w3 = Wand(5, 4, 0.2)
        w4 = Wand(5, 4, 0.2)
        r = Raum(hoehe=12, bezeichnung="PetersRaum",
                 raumnummer=200, waende=(w1, w2, w3, w4))
        r.print_me()
        print("Willkommen im Raumplaner")
        print("hier können sie Ihr virtuelles Gebäudemodell verwalten!")
        print(r.raumbuch())

        # print raumbuch into text file
