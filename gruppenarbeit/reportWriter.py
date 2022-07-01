from door import Tuer
from window import Fenster
from opening import Oeffnung

class Report:
    numbering = 0

    def __init__(self):
        self.numbering = 0

    def write(self, raum):
        self.numbering = self.numbering + 1  # increment the numbering
        return f"{self.numbering}" + raum.print_me()
        # ohne Leerzeichen, da dies in der Print-Funktion bereits vorhanden ist

    @staticmethod
    def write_windows(windows_list) -> str:
        res = ""
        for i, windowL in enumerate(windows_list):
            res = res + f"{i}" + "\n\n"
            print(len(windowL))
            for x, window in enumerate(windowL):
                res = res + f"Raum {i} Fenster,{x}" + window.print_me() + "\n\n"
        return res

    @staticmethod
    def write_doors(doors_list) -> str:
        res = ""
        for i, doorL in enumerate(doors_list):
            for x, door in enumerate(doorL):
                res = res + f"Raum {i} Tuer,{x} " + door.print_me() + "\n\n"
        return res

    @staticmethod
    def write_header(line, vn1, nn1, mn1, vn2, nn2, mn2):
        separator = ", "
        width_of_details_1 = len(vn1) + len(nn1) + len(mn1) + len(separator)
        width_of_details_2 = len(vn2) + len(nn2) + len(mn2) + len(separator)
        space_for_1 = " " * (len(line) - width_of_details_1)
        space_for_2 = " " * (len(line) - width_of_details_2)

        ausgabe_namen = f"{nn1}{separator}{vn1}{space_for_1}{mn1}\n{nn2}{separator}{vn2}{space_for_2}{mn2}\n" \
                        f"{line}\n"
        return ausgabe_namen
