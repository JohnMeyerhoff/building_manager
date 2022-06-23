from opening import Oeffnung
class Tuer(Oeffnung):

    smoke_protection = False
    emergency_exit = False
    manufacturer = ""

    def __init__(self, rauchschutz, notausgang, hersteller):
        self.smoke_protection = rauchschutz
        self.emergency_exit = notausgang
        self.manufacturer = hersteller
        super(Tuer,self).__init__()
