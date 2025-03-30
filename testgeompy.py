from geompy import Kwadrat, Prostokat, Kolo, Szescian, Prostopadloscian, Kula

# Test figur 2D
print("Figury 2D:")
kwadrat = Kwadrat(5)
print(f"Kwadrat - pole: {kwadrat.pole()}, obwód: {kwadrat.obwod()}")

prostokat = Prostokat(4, 6)
print(f"Prostokąt - pole: {prostokat.pole()}, obwód: {prostokat.obwod()}")

kolo = Kolo(3)
print(f"Koło - pole: {kolo.pole():.2f}, obwód: {kolo.obwod():.2f}")

# Test figur 3D
print("\nFigury 3D:")
szescian = Szescian(4)
print(f"Sześcian - objętość: {szescian.objetosc()}, pole: {szescian.pole_powierzchni()}")

prostopadloscian = Prostopadloscian(3, 4, 5)
print(f"Prostopadłościan - objętość: {prostopadloscian.objetosc()}, pole: {prostopadloscian.pole_powierzchni()}")

kula = Kula(3)
print(f"Kula - objętość: {kula.objetosc():.2f}, pole: {kula.pole_powierzchni():.2f}")