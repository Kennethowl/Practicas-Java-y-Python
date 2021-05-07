# Simulacion de un cajero automatico
from os import system

saldo = 2000

while True:
    system("cls")
    print("1 - Consultar")
    print("2 - Retiros")
    print("3 - Depositos")
    print("4 - Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print(f"Saldo en tu cuenta es: {saldo}")
        system("pause > null")
    elif opcion == 2:
        retiro = int(input("Retira la cantidad deseada: "))
        if retiro > saldo:
            print("No posee esa cantidad en su cuenta")
            system("pause > null")
        else:
            saldo = int(saldo) - retiro
            print(f"Saldo disponible: {saldo}")
            system("pause > null")
    elif opcion == 3:
        deposito = int(input("Deposite la cantidad deseada: "))
        saldo = int(saldo) + deposito
        print(f"Saldo disponible: {saldo}")
        system("pause > null")
    elif opcion == 4:
        print("Operacion Realizada")
        break