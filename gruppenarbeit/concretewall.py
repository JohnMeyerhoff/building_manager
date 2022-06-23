from opening import Wand


class Stahlbetonwand(Wand):
    steel_density = 0.0
    concrete_density = 0.0
    concrete_class = 0.0
    retention_amount = 0.0

    def __init__(self, stahldichte, betondichte, betonfestigkeitsklasse, bewehrungsgehalt):
        self.steel_density = stahldichte
        self.concrete_density = betondichte
        self.concrete_class = betonfestigkeitsklasse
        self.retention_amount = bewehrungsgehalt
        super(Stahlbetonwand, self).__init__()