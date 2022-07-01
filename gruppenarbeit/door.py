from opening import Oeffnung


class Tuer(Oeffnung):
    smoke_protection = False
    emergency_exit = False
    manufacturer = ""

    def __init__(self, rauchschutz, notausgang, hersteller, breite, hoehe, durchmesser):
        super(Tuer, self).__init__(hoehe, breite, durchmesser)
        self.smoke_protection = rauchschutz
        self.emergency_exit = notausgang
        self.manufacturer = hersteller
