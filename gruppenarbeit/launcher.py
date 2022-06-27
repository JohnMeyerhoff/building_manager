# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:58:01 2022

@author: john
"""
from room import Raum
from wall import Wand
from opening import Oeffnung
from prompt_toolkit import prompt


class Launcher:
    
    @staticmethod
    def run():
        # annotation aus SonarLint  (python:S5719)
        w1 = Wand(5, 4, 0.2)
        w2 = Wand(5, 4, 0.2)
        w3 = Wand(5, 4, 0.2)
        w4 = Wand(5, 4, 0.2)
        o1 = Oeffnung(2, 1, 5)
        r = Raum(hoehe=12, bezeichnung="PetersRaum",
                 raumnummer=200, waende=(w1, w2, w3, w4))
        r.print_me()
        print("Willkommen im Raumplaner")
        print("hier können sie Ihr virtuelles Gebäudemodell verwalten!")

        text = prompt('Give me some input: ')

        with open('readme.txt', 'w') as f:
            f.write(text)

        print(r.raumbuch())
        print(o1.print_me())

        # print raumbuch into text file
