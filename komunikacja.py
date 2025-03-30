class Komunikacja:
    def __init__(self, odbiorca, tresc):
        self.odbiorca = odbiorca
        self.tresc = tresc


    def wyslij_wiadomosc(self):
        print(f"Wiadomosc do {self.odbiorca} o tresci: {self.tresc}")