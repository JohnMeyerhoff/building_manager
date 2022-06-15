# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:58:01 2022

@author: john
"""
from room import Raum
from tkinter import *

r = Raum(hoehe=12, bezeichnung="PetersRaum", raumnummer=200)
r.printMe()

#start the gui using tkinter
root = Tk()
root.title("Raumplaner")
root.geometry("700x300")
#create a label in root window
label = Label(root, text="Willkommen im Raumplaner")
label.pack()

raum1 = Label(root, text=r.printMe())
raum1.pack()

# open the gui
root.mainloop()
