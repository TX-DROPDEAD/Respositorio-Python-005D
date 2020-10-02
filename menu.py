import os

def Numeros():
    num = int(input("Ingrese la cantidad de números que desea verificar: "))
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(num):
        a = int(input("Ingrese el digito: "))
        if (a > 0):
            b = b + 1
        elif (a == 0):
            c = c + 1
        elif (a < 0):
            d = d + 1
    
    print("Números positivos: "+ str(b))
    print("Números negativos: "+ str(d))
    print("Números en cero: "+ str(c))  
    pausa = print("Presione una tecla para continuar...")   

def Personas():
    n = int(input("Ingrese numero de personas: "))
    a = 0
    sum = 0
    for i in range(n):
        nom = input("Ingrese nombre de la persona: ")
        a = int(input("Ingrese edad de la persona: "))
        sum = sum + a

    print("Promedio de las edades: " + str(sum/n))
    pausa = input("Presione una tecla para continuar..")   

seguir = True

while(seguir):
    os.system('cls')
    print("------ Menú Principal ------")
    print("1.- Números")
    print("2.- Personas")
    print("3.- Finalizar")

    opcion = int(input("Diguite una opción: "))

    if (opcion == 1):
        Numeros()
    if (opcion == 2):
        Personas()
    if (opcion == 3):
        seguir = False
        break

