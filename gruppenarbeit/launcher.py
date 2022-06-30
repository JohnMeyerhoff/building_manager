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

        print("\n\nWillkommen im Raumplaner")
        print("hier können sie Ihr virtuelles Gebäudemodell verwalten!")

        print("Bitte geben sie zuerst einige Informationen zu den Teilnehmern ein:\n\n")
        vn1 = prompt("Bitte geben sie den Vorname des 1. Teilnehmers ein: ")
        nn1 = prompt("Bitte geben sie den Nachnamen des 1. Teilnehmers ein: ")
        mn1 = prompt("Bitte geben sie die Matrikelnummer des 1. Teilnehmers ein: ")
        vn2 = prompt("Bitte geben sie den Vorname des 2. Teilnehmers ein: ")
        nn2 = prompt("Bitte geben sie den Nachnamen des 2. Teilnehmers ein: ")
        mn2 = prompt("Bitte geben sie die Matrikelnummer des 2. Teilnehmers ein: ")

        short_line = "-" * 25
        line = "-" * 90
        ausgabe_namen = Report.write_header(line, vn1, nn1, mn1, vn2, nn2, mn2)
        ende = f"{line}\nEnde des Berichts"
        exit_message = f"\n{line}\nDas Programm ist beendet, die Ausgabe befindet sich in der Datei bericht.txt"

        # Speichern einer Datei mit Umlauten https://stackoverflow.com/a/934203
        rooms = f"Raumbuch\n{short_line}\n"
        # rooms = rooms + report_writer.write(Launcher.get_room_from_console())
        rooms = rooms + f"\n"

        report_writer = Report()
        with codecs.open("bericht.txt", "w", "utf-8-sig") as bericht:
            bericht.write(ausgabe_namen)
            bericht.write(rooms)
            bericht.write(ende)

        print(exit_message)

        # print raumbuch into text file

    @staticmethod
    def get_room_from_console():
        w1 = Wand(5, 4, 0.2)
        w2 = Wand(5, 4, 0.2)
        w3 = Wand(5, 4, 0.2)
        w4 = Wand(5, 4, 0.2)
        o1 = Oeffnung(2, 1, 5)

        bezeichnung = prompt('Raumbezeichnung: ')
        hoehe = prompt('Raumhöhe: ')
        breite = prompt('Breite: ')

        return Raum(hoehe=hoehe, bezeichnung=bezeichnung, raumnummer=5, waende=(w1, w2, w3, w4))
