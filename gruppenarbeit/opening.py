class Oeffnung:
    height = 0.0
    width = ""
    diameter = 0

    def __init__(self, hoehe, breite, durchmesser):
        self.height = hoehe
        self.width = breite
        self.diameter = durchmesser

    def print_me(self):
        return f"Öffnung: Breite: {self.width}, Durchmesser: {self.diameter}, Höhe (in m): {self.height}"
