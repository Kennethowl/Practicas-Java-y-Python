from os import system

while True:
    system("cls")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("0 - Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        a = int(input("Ingrese a: "))
        b = int(input("Ingrese b: "))
        suma = a + b
        print(f"{a} + {b} = {suma}")
        system("pause > null")
    elif opcion == 2:
        a = int(input("Ingrese a: "))
        b = int(input("Ingrese b: "))
        resta = a - b
        print(f"{a} - {b} = {resta}")
        system("pause > null")
    elif opcion == 3:
        a = int(input("Ingrese a: "))
        b = int(input("Ingrese b: "))
        multiplicacion = a * b
        print(f"{a} * {b} = {multiplicacion}")
        system("pause > null")
    elif opcion == 4:
        a = int(input("Ingrese a: "))
        b = int(input("Ingrese b: "))
        division = a / b
        print(f"{a} / {b} = {division}")
        system("pause > null")
    if opcion == 0:
        print("Finalizar programa")
        break