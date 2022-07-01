from opening import Oeffnung


class Fenster(Oeffnung):
    sound_protection_class = ""
    u_value = 0.0
    manufacturer = ""
    brh = 0.0

    def __init__(self, schallschutzklasse, u_wert, hersteller, brh, breite, hoehe, durchmesser):
        super(Fenster, self).__init__(hoehe, breite, durchmesser)
        self.sound_protection_class = schallschutzklasse
        self.u_value = u_wert
        self.manufacturer = hersteller
        self.brh = brh

    def print_me(self):
        return f"Fenster: Breite: {self.width}, Durchmesser: {self.diameter}, Höhe (in m): {self.height}"
