n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n1 > n2:
    print(f"El numero mayor entre n1 y n2 es: {n1}")
elif n2 > n1:
    print(f"El numero mayor entre n1 y n2 es: {n2}")
else:
    print(f"Ambos son iguales: {n1} - {n2}")
