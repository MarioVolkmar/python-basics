## Imprimir números del 1 al 10
for i in range(1 , 11):
    print (i)

## Imprimir números del 10 al 1

for i in range (10, 0 , -1 ):
    print (i)


## Números pares del 1 al 20

for i in range (1 , 21):
    if i % 2 == 0:
        print(i)

## Números impares del 1 al 20

for i in range (1 , 21):
    if i % 2 != 0:
        print(i)

## Tabla de multiplicar

numero = 8

for i in range (1 , 11):
    print(f"{numero} x {i} = {numero * i}")

## Suma de números del 1 al 100

suma = 0

for i in range (1 , 101):
    suma += i

print(suma)

## Suma de números pares del 1 al 100

suma = 0

for i in range (1 , 101):
    if i % 2 == 0:
        suma += i

print(suma)

## Contar números divisibles por 3

contador = 0

for i in range (1, 101):
    if i % 3 == 0 :
        contador += 1

print(f"Hay un total de {contador} numeros divisibles por 3 del 1 al 100")

## Recorrer una palabra

palabra = "Python"

for letra in palabra:
    print(letra)

## Contar vocales en una palabra

vocales = "aeiuo"

palabra = "programacion"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"Hay un total de {contador} vocales en la palabra {palabra}")

