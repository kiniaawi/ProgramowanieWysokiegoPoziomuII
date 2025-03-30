from osoba import Osoba


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        Osoba.__init__(self, imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self, stanowisko, pensja):
        return (f"Pracuje jako {stanowisko}, zarabiam {pensja} zl.")