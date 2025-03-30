import math


class Szescian:
    def __init__(self, bok):
        self.bok = bok

    def objetosc(self):
        return self.bok ** 3

    def pole_powierzchni(self):
        return 6 * self.bok ** 2


class Prostopadloscian:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def objetosc(self):
        return self.a * self.b * self.c

    def pole_powierzchni(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)


class Kula:
    def __init__(self, r):
        self.r = r

    def objetosc(self):
        return (4 / 3) * math.pi * self.r ** 3

    def pole_powierzchni(self):
        return 4 * math.pi * self.r ** 2