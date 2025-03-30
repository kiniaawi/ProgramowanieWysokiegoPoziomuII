class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        print(f"\nDzielo o tytule {self.tytul}, autorstwa: {self.autor}, rok wydania: {self.rok_wydania}")

