# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:58:01 2022

@author: john
"""
from room import Raum
from wall import Wand
from opening import Oeffnung
from prompt_toolkit import prompt
import codecs


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

        bezeichnung = prompt('Raumbezeichnung: ')
        hoehe = prompt('Raumhöhe: ')
        breite = prompt('Breite: ')

        raum = Raum(hoehe=hoehe, bezeichnung=bezeichnung, raumnummer=5, waende=(w1, w2, w3, w4))

        # Speichern einer Datei mit Umlauten https://stackoverflow.com/a/934203
        with codecs.open("bericht.txt", "w", "utf-8-sig") as bericht:
            bericht.write(raum.print_me())

        print(r.raumbuch())
        print(o1.print_me())

        # print raumbuch into text file
