# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:58:01 2022

@author: john
"""
import codecs
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError

from door import Tuer
from opening import Oeffnung
from reportWriter import Report
from room import Raum
from wall import Wand
from window import Fenster


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
        ende = f"\n{line}\nEnde des Berichts"
        exit_message = f"\n{line}\nDas Programm ist beendet, die Ausgabe befindet sich in der Datei bericht.txt"

        # Speichern einer Datei mit Umlauten https://stackoverflow.com/a/934203
        rooms = f"Raumbuch\n{short_line}\n"  # kein Doppelpunkt hier
        doors = f"Türliste:\n{short_line}\n"
        windows = f"Fensterliste:\n{short_line}\n"
        room_list = []

        eingabe = "leer"
        while eingabe != "nein" and eingabe != "Nein" and eingabe != "n":
            room_list.append(Launcher.get_room_from_console())
            eingabe = prompt("Möchten Sie einen weiteren Raum eingeben? (ja/nein) ")
        report_writer = Report()
        windows_list = [room.get_windows() for room in room_list]
        doors_list = [room.get_doors() for room in room_list]
        with codecs.open("bericht.txt", "w", "utf-8-sig") as bericht:
            bericht.write(ausgabe_namen)
            bericht.write(rooms)
            for i, room in enumerate(room_list):
                bericht.write(f"{i}" + room.raumbuch() + "\n\n")
            bericht.write(doors)
            bericht.write(Report.write_doors(doors_list))
            bericht.write(windows)
            bericht.write(Report.write_windows(windows_list))
            bericht.write(ende)

        print(exit_message)

        # print raumbuch into text file

    @staticmethod
    def get_room_from_console():

        o1 = Oeffnung(2, 1, 5)

        bezeichnung = prompt('Raumbezeichnung: ')
        float_validator = Validator.from_callable(Launcher.zahl_ok, error_message='Invalid input')
        nummer = prompt('Nummer: ', validator=float_validator)

        print("\nBitte geben sie die Wände ein:")

        wall_list: [Wand] = []
        for i in 0, 1, 2, 3:
            print(f"\nEingabe Wand {i + 1}:")
            wall_list.append(Launcher.get_wall_from_console())
            print("\n")
            print(wall_list[i].print_me())
            eingabe = prompt("Möchten Sie eine Öffnung für die Wand eingeben? (ja/nein) ")
            while eingabe != "nein" and eingabe != "Nein" and eingabe != "n":
                oeffn = Launcher.get_opening_from_console()
                wall_list[i].add_opening(oeffn)
                print(oeffn.print_me())
                eingabe = prompt("Möchten Sie eine weitere Öffnung für die Wand eingeben? (ja/nein) ")

        return Raum(hoehe=wall_list[0].height, bezeichnung=bezeichnung, raumnummer=int(nummer),
                    waende=(wall_list[0], wall_list[1], wall_list[2], wall_list[3]))

    @staticmethod
    def get_wall_from_console() -> Wand:
        float_validator = Validator.from_callable(Launcher.zahl_ok,
                                                  error_message='Bitte geben Sie eine Zahl ein "." als Dezimalzeichen')
        breite = prompt('Breite: ', validator=float_validator)
        hoehe = prompt('Höhe: ', validator=float_validator)
        dicke = prompt('Dicke: ', validator=float_validator)
        return Wand(float(breite), float(hoehe), float(dicke))

    @staticmethod
    def get_opening_from_console() -> Oeffnung:
        float_validator = Validator.from_callable(Launcher.zahl_ok,
                                                  error_message='Bitte geben Sie eine Zahl ein "." als Dezimalzeichen')
        fenster_oder_tuer = Validator.from_callable(Launcher.opening_ok,
                                                    error_message='Bitte geben Sie "Fenster" oder "Tür" ein (oder F/T)')

        kind = prompt('Art der Öffnung: (Fenster/Tür) ', validator=fenster_oder_tuer)
        if kind == "f" or kind == "F" or kind == "Fenster":
            kind = "Fenster"
        elif kind == "t" or kind == "T" or kind == "Tür":
            kind = "Tür"
        breite = prompt('Breite: ', validator=float_validator)
        hoehe = prompt('Höhe: ', validator=float_validator)
        durchmesser = prompt('Durchmesser: ', validator=float_validator)
        if kind == "Fenster":
            schallschutzklasse = prompt('Schallschutzklasse: ')
            u_wert = prompt('U-Wert: ', validator=float_validator)
            hersteller = prompt('Hersteller: ')
            brh = prompt('Brh: ', validator=float_validator)
            return Fenster(schallschutzklasse, float(u_wert), hersteller, float(brh), float(breite), float(hoehe),
                           float(durchmesser))
        else:
            rauchschutz = prompt('Rauchschutz: (ja/nein) ') == "ja"
            notausgang = prompt('Notausgang: (ja/nein) ') == "ja"
            hersteller = prompt('Hersteller: ')
            return Tuer(rauchschutz, notausgang, hersteller, float(breite), float(hoehe),
                        float(durchmesser))

    # aus der Dokumentation

    @staticmethod
    def zahl_ok(eingabe):
        try:
            float(eingabe)
            return True
        except ValueError:
            return False

    @staticmethod
    def opening_ok(eingabe):
        if eingabe == "f" or eingabe == "F" or eingabe == "Fenster" or eingabe == "t" or eingabe == "T" or eingabe == "Tür":
            return True
        else:
            return False
