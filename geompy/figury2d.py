import math


class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2

    def obwod(self):
        return 4 * self.bok


class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * (self.a + self.b)


class Kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return math.pi * self.r ** 2

    def obwod(self):
        return 2 * math.pi * self.r