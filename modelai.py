import json

class ModelAI:
    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        ModelAI.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return (f"Liczba utworzonych modeli: {cls.liczba_modeli}\n")

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, "r") as f:
            text = json.load(f)
            nazwa_modelu = text["nazwa_modelu"]
            wersja = text["wersja"]
        return f"Model z pliku: {nazwa_modelu} wersja: {wersja}\n"


