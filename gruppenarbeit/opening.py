class Oeffnung:
    height = 0.0
    width = 0.0
    diameter = 0

    def __init__(self, hoehe, breite, durchmesser):
        self.height = hoehe
        self.width = breite
        self.diameter = durchmesser

    def print_me(self):
        return f"Öffnung: Breite: {self.width}, Durchmesser: {self.diameter}, Höhe (in m): {self.height}"

    def vob_sub_area(self):
        if self.area() < 2.500:
            return 0.0
        else:
            return self.area()

    def area(self):
        """
         wird verwendet, um später zu prüfen, ob nach der
        Abrechnungsvorschrift der VOB die Fläche der Öffnung von der
        Fläche der Wand abgezogen werden darf.
        :return: fläche der Öffnung
        """
        return self.width * self.height
