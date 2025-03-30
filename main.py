import modelai
import matrix
from ebook import Ebook
from komunikacja import Komunikacja
from ksiazka import Ksiazka
from pracownik import Pracownik
from manager import Manager
from rozrywka import Rozrywka
from smartphone import Smartphone
from userauth import UserAuth
from library import Library

#---ZAJ 1---
print("ZAJECIA 1")
#zad1
model1 = modelai.ModelAI("model_1", 3.4)
print(f"Stworzny model: {model1.nazwa_modelu} wersja: {model1.wersja}")
print(model1.z_pliku("my_file.json"))
print(model1.ile_modeli())
print("---------------")

#zad2
matrix1 = matrix.Matrix(2, 3, 2, 3)
matrix2 = matrix.Matrix(5, 6, 5, 7)

matrix3 = matrix1 + matrix2
matrix4 = matrix1 * matrix2

print(matrix3)
print(matrix4)

print(repr(matrix3))
print(repr(matrix4))
print("---------------")

#zad3
pracownik1 = Pracownik("Jan", "Kowalski", 34, "IT", 5400)
pracownik2 = Pracownik("Janina", "Kowalska", 34, "IT", 5400)

pracownik1.przedstaw_sie()
pracownik2.przedstaw_sie()

manager = Manager("Adam", "Rybak", 54, "Manager", 7600)
manager.przedstaw_sie()
manager.dodaj_do_zespolu(pracownik1)
manager.przedstaw_sie()
manager.dodaj_do_zespolu(pracownik2)
manager.przedstaw_sie()

#---ZAJ 2---
#zad1
print(f"\n\nZAJECIA 2")
ksiazka = Ksiazka("Spiacy ksiaze", "Stephanie Mayer", 2007)
ksiazka.opis()

ebook = Ebook("Spiacy ksiaze", "Stephanie Mayer", 2008, 278)
ebook.opis()

#zad2
komunikacja = Komunikacja("Mama", "BRB")
rozrywka = Rozrywka("Elton John - Goodbye Yellow Brick Roads")
smartphone = Smartphone("Galaxy S10", "Samsung", komunikacja, rozrywka)
smartphone.komunikacja.wyslij_wiadomosc()
smartphone.rozrywka.odtworz_muzyke()

#zad3
auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
   auth.login("admin", "1234")
   auth.login("unknown", "pass")
   auth.login("user", "wrongpass")
except Exception as e:
   print(e)

try:
   auth.login("user", "wrongpass")
except Exception as e:
   print(f"Blad: {e}")


#zad4
list = [2.5, 2.3, 6.7, 5.6, 1.5, 9.9, 7.6, 4.4]

def average(numbers):
    return sum(numbers) / len(numbers)

avg = average(list)
print(f"\n\nSrednia: {avg}")

#zad5
books_data = [
    {"ISBN": "1234", "title": "Python Basics"},
    {"ISBN": "4567", "title": "Advanced Python"},
]

book = Library(books_data )
book.find_book("1234")

