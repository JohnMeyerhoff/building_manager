# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:58:01 2022

@author: john
"""
from gruppenarbeit.room import Raum


class Launcher:
    height = 0.0
    name = ""
    number = 0

    @staticmethod
    def run():
        # annotation aus SonarLint  (python:S5719)

        r = Raum(hoehe=12, bezeichnung="PetersRaum", raumnummer=200)
        r.print_me()
        print("Willkommen im Raumplaner")
        print("hier können sie Ihr virtuelles Gebäudemodell verwalten!")


        print(r.raumbuch())
