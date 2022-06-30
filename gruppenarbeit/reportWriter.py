class Report:
    numbering = 0

    def __init__(self):
        self.numbering = 0

    def write(self, raum):
        self.numbering = self.numbering + 1  # increment the numbering
        return f"{self.numbering}" + raum.print_me()
        # ohne Leerzeichen, da dies in der Print-Funktion bereits vorhanden ist
