from ksiazka import Ksiazka


class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        Ksiazka.__init__(self, tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        super().opis()
        print(f"Rozmiar: {self.rozmiar_pliku} MB")