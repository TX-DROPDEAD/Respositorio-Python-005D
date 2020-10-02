
a = int(input("Digite un número: "))
b = int(input("Digite otro número: "))

suma = a + b
multi = a * b 

print("La suma de "+ str(a) + "y de "+ str(b)+ "es igual a "+ str(suma))
print("La multiplicación de "+ str(a) + "y de "+ str(b)+ "es igual a "+ str(multi))

if(a > b):
    print("El número " + str(a)+ " es mayor que: " + str(b))
elif(a < b):
    print("El número " + str(b)+ " es mayor que: " + str(a))
else:
    print("Los números son iguales!")