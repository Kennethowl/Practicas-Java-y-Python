from os import system
import math

a = int(input("Ingresa a: "))
while a == 0:
    print("Digite un numero distinto de 0!")
    a = int(input("Ingresa a: "))

b = int(input("Ingresa b: "))
c = int(input("Ingresa c: "))

determinante = b * b - 4 * a * c

if determinante > 0:
    x1 = (-b + math.sqrt(determinante)) / (2 * a)
    x2 = (-b - math.sqrt(determinante)) / (2 * a)
    print(f"X1 = {x1} y X2 = {x2}")
elif determinante == 0:
    x1 = (-b)/(2*a)
    print(f"X1 = {x1}")
else:
    print("No tiene solucion!")