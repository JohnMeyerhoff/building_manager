class Wand:
    length = 0.0
    height = 0.0
    thickness = 0.0
    # Beziehungsrichtung hier von der Wand aus, Liste kann leer sein
    openings = []

    def __init__(self, laenge, hoehe, dicke):
        self.length = laenge
        self.height = hoehe
        self.thickness = dicke

    def add_opening(self, opening):
        self.openings.append(opening)

    def print_me(self):
        return f"Wand, L, H, B: {self.length}, {self.height},  {self.thickness}"

    def wall_area(self):
        return 1.0 * self.length * self.height

    def vob_wall_area(self):
        area = self.wall_area()
        for opening in self.openings:
            area -= opening.vob_sub_area()
        return area
