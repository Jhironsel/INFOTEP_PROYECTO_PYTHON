inicio = 1
pares = []
impares = []

while inicio <= 100:
    if inicio % 2 == 0:
        pares.append(inicio)
    else:
        impares.append(inicio)
    inicio = inicio + 1

print("Numeros pares del 1 al 100:")
print(pares)
print("Numeros impares del 1 al 100:")
print(impares)

print("")
print("Utilizando la magia de la programación ingrese un numero:")
inicio = int(input())

if inicio % 2 == 0:
    print("El numero "+str(inicio)+" es un numero par.")
else:
    print("El numero "+str(inicio)+" es un numero impar.")


print("")
print("Continuando con este mundo magico de la programación ingrese otro numero:")
inicio = int(input())

if inicio < 0:
    print("El numero "+str(inicio)+" es un numero NEGATIVO.")
elif inicio == 0:
    print("Dicho numero 0 es el numero neutro.")
else:
    print("El numero "+str(inicio)+" es un numero POSITIVO.")
