# Напишите программу, вычисляющую площадь всех граней и объем прямоугольного параллелепипеда.
# Формат входных данных: даны три целые числа - ширина, высота и длина параллелепипеда.
# Формат выходных данных: вывести площадь всех граней и объем фигуры

# Важно!
# Оформите решение так, что работа с вашей программой была удобна пользователю.
# Пользователь должен понимать, что его просят ввести и что именно делает программа.

a = int(input("Введите ширину прямоугольного параллелепипеда: "))
b = int(input("Введите высоту прямоугольного параллелепипеда: "))
c = int(input("Введите длину прямоугольного параллелепипеда: "))

S1 = a*b
S2 = b*c
S3 = a*c

P = S1 + S2 + S3
V = a * b * c

print("S - граней параллелепипеда: ", P)
print("V - прямоугольного параллелепипеда", V)

