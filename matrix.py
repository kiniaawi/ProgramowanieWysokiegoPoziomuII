class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print(f"Macierz postaci: \na b \nc d \nWartosci: \n{a} {b} \n{c} {d}\n\n")

    def __add__(self, other):
        return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __mul__(self, other):
        return Matrix(self.a * other.a, self.b * other.b, self.c * other.c, self.d * other.d)

    def __str__(self):
        return f"Macierz \n[{self.a}, {self.b}, \n{self.c}, {self.d}]\n"

    def __repr__(self):
        return f"Macierz([{self.a}, {self.b}, {self.c}, {self.d}])"