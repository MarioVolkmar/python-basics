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

## Contar letras específicas

texto = "banana"
letra = "a"
contador = 0

for l in texto:
    if l == letra:
        contador += 1

print(f"La letra {letra} aparece un total de {contador} veces en la palabra {texto}")


## Invertir una palabra

palabra = "python"

invertida = ""

for i in range (len(palabra) - 1, -1 , -1):
    invertida += palabra[i]

print(invertida)

## Sumar elementos de una lista

numeros = [5, 10, 15, 20]

suma = 0

for n in numeros :
    suma += n

print(suma)

## Encontrar el número mayor

numeros = [8, 3, 15, 1, 20, 7]
mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print(mayor)

## Encontrar el número menor

numeros = [8, 3, 15, 1, 20, 7]
menor = numeros[0]

for n in numeros:
    if n < menor:
        menor = n

print(menor)

## Contar positivos y negativos

numeros = [3, -1, 5, -7, 0, 9, -2]
positivos = 0
negativos = 0
ceros = 0

for n in numeros:
    if n == 0 :
        ceros += 1
    elif n > 0 :
        positivos += 1
    elif n < 0 :
        negativos += 1

print(f"Positivos: {positivos} - Negativos: {negativos} - Ceros: {ceros}")

## Promedio de una lista

notas = [4.2, 3.8, 5.0, 2.9, 4.5]

suma = 0

for n in notas :
    suma += n

promedio = suma / len(notas)

print(f"El promedio es del {promedio:.2f}")

## Validar contraseña con intentos

password_correcta = "123"
intentos = 0

while True:
    intentos += 1
    password = input("Ingrese la contraseña ")
    if password == password_correcta :
        print(f"Acceso concedido, te tomo {intentos} intentos")
        break

## Menú simple con while

while True:
    respuesta = input("'1' Para saludar - ''2' Para mostrar objetivo - '3' Para salir ")
    if respuesta == "1":
        print("Hola Mario")
    elif respuesta == "2" :
        print("Estoy aprendiendo Backend con Python")
    elif respuesta == "3" :
        print("Programa finalizado")
        break
    else:
        print("Ingreso invalido")

## Mini sistema de ahorro

meta = 100000
ahorro = 0

while ahorro < meta :
    ingreso = 0
    while ingreso <= 0:
        ingreso = float(input("Ingrese un valor a ahorrar valido (Mayor o igual a cero) "))
    ahorro += ingreso

print(f"Meta alcanzada, el ahorro fue de {ahorro}")
