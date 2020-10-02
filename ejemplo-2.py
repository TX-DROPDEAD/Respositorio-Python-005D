
ingresos=int(input("¿cuantos números desea ingresar?: "))

par = 0
impar = 0

for x in range(ingresos):
    numero=int(input("Ingrese un número: "))
    if (numero%2==0):
        par=par+1
    elif(numero%2!=0):
        impar=impar+1

print("La cantidad de números pares es: " + str(par))
print("La cantidad de números impares es: " + str(impar))