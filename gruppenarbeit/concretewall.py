from opening import Wand


class Stahlbetonwand(Wand):
    # ToDo: stahldichte etc aus diagramm übernehmen
    kind = ""
    visible = False

    def __init__(self, steinsorte, sichtmauerwerk):
        self.kind = steinsorte
        self.visible = sichtmauerwerk
        super(Stahlbetonwand, self).__init__()

    def print_me(self):
        if(self.visible):
            sm = "ja"
        else:
            sm = "nein"
        return f"Mauerwerk Sorte: {self.kind} Sichtmauerwerk: {sm}, L, H, B: {self.length}, {self.height},  {self.thickness}"
