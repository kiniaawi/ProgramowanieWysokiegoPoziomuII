import modelai
import matrix

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
