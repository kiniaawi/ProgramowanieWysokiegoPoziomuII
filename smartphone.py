from telefon import Telefon


class Smartphone(Telefon):
    def __init__(self, model, producent, komunikacja, rozrywka):
        Telefon.__init__(self, model, producent)
        self.komunikacja = komunikacja
        self.rozrywka = rozrywka