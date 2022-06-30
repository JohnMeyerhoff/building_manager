# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:58:01 2022

@author: john
"""
from room import Raum
from wall import Wand
from opening import Oeffnung
from prompt_toolkit import prompt
from reportWriter import Report
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

        print("Bitte geben sie zuerst einige Informationen zu den Teilnehmern ein:")
        vn1 = prompt("Bitte geben sie den Vorname des 1. Teilnehmers ein: ")
        nn1 = prompt("Bitte geben sie den Nachnamen des 1. Teilnehmers ein: ")
        mn1 = prompt("Bitte geben sie die Matrikelnummer des 1. Teilnehmers ein: ")
        vn2 = prompt("Bitte geben sie den Vorname des 2. Teilnehmers ein: ")
        nn2 = prompt("Bitte geben sie den Nachnamen des 2. Teilnehmers ein: ")
        mn2 = prompt("Bitte geben sie die Matrikelnummer des 2. Teilnehmers ein: ")
        line = "-" * 50
        ausgabe_namen = f"{nn1}, {vn1} \t\t\t\t {mn1}\n{nn2}, {vn2}  \t\t\t\t {mn2}\n" \
                        f"{line}\n "

        bezeichnung = prompt('Raumbezeichnung: ')
        hoehe = prompt('Raumhöhe: ')
        breite = prompt('Breite: ')

        raum = Raum(hoehe=hoehe, bezeichnung=bezeichnung, raumnummer=5, waende=(w1, w2, w3, w4))
        report_writer = Report()
        # Speichern einer Datei mit Umlauten https://stackoverflow.com/a/934203
        with codecs.open("bericht.txt", "w", "utf-8-sig") as bericht:
            bericht.write(ausgabe_namen)
            bericht.write(report_writer.write(raum))

        print(r.raumbuch())
        print(o1.print_me())

        # print raumbuch into text file
