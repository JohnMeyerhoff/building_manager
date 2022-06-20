from opening import Oeffnung
class Tuer(Oeffnung):

    height = 0.0
    name = ""
    number = 0

    def __init__(self, hoehe, bezeichnung, raumnummer):
        self.height = hoehe
        self.name = bezeichnung
        self.number = raumnummer

    def print_me(self):
        return f"Raum {self.number}: Bezeichnung: {self.name}, Höhe (in m): {self.height}"
