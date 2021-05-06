for a in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print(f"{a} * {a} = {a ** 2}")

i = input ("Ingrese el primer rango: ")
j = input ("Ingrese el segundo rango: ") 
for i in range(int(i), int(j)):
    print(f"{i} + {i} = {i + i}")