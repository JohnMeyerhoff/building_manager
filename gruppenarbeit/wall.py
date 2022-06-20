class Wand:
    length = 0.0
    height = 0.0
    thickness = 0.0

    def __init__(self, laenge, hoehe,  dicke):
        self.length = laenge
        self.height = hoehe
        self.thickness = dicke

    def print_me(self):
        return f"Wand, L, H, B: {self.length}, {self.height},  {self.thickness}"
