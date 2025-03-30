from pracownik import Pracownik


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        Pracownik.__init__(self, imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = []

    def przedstaw_sie(self):
        podwladni = ', '.join([f"{p.imie} {p.nazwisko}" for p in self.zespol]) or "brak podwładnych"
        print(f"Jestem {self.imie} {self.nazwisko}, mam podwładnych: {podwladni}.")

    def dodaj_do_zespolu(self, pracownik):
        if isinstance(pracownik, Pracownik):  # Sprawdzamy, czy dodajemy obiekt klasy Pracownik
            self.zespol.append(pracownik)
        else:
            raise ValueError("Do zespołu można dodać tylko obiekt klasy Pracownik.")
