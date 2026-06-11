## Clasificador de números

numero = -8

if numero == 0 :
    print("El numero es cero")
elif numero > 0:
    if numero % 2 == 0:
        print("El numero es un positivo par")
    else:
        print("El numero es positivo impar")
else:
    if numero % 2 == 0:
        print("El numero es un negativo par")
    else:
        print("El numero es negativo impar")

## Suma de pares e impares

suma_pares = 0
cantidad_pares = 0
suma_impares = 0
cantidad_impares = 0

for i in range ( 1 , 51):
    if i % 2 == 0:
        suma_pares += i
        cantidad_pares += 1
    else:
        suma_impares += i
        cantidad_impares += 1

print(f"Cantidad pares: {cantidad_pares} \nSuma pares: {suma_pares} \nCantidad impares: {cantidad_impares} \nSuma impares: {suma_impares}")

## Contador de vocales y consonantes

texto = "backend python"

vocales = "aeiou"
cantidad_vocales = 0
cantidad_consonantes = 0

for letra in texto:
    if letra in vocales:
        cantidad_vocales += 1
    elif letra != " ":
        cantidad_consonantes += 1

print(f"Vocales: {cantidad_vocales} \nConsonantes: {cantidad_consonantes}")

## Validador de contraseña simple

password = "Python123"
tiene_mayus = False
tiene_numero = False
numeros = "1234567890"

if len(password) >= 8:
    for i in password:
        if i in numeros:
            tiene_numero = True
        elif i == i.upper():
            tiene_mayus = True
    print ("Contraseña Valida") if tiene_mayus and tiene_numero else print("Contraseña Invalida")
else:
    print("Contraseña demasiado corta")

## Promedio y estado de notas

notas = [4.2, 3.5, 2.8, 5.0, 4.0]

suma = 0

for n in notas:
    suma += n

promedio = suma / len(notas)

print(f"Aprobado - Nota Definitiva: {promedio:.2f}") if promedio >= 3 else print(f"Desaprobado - Nota Definitiva: {promedio:.2f}")

## Mayor y menor de una lista

numeros = [12, 45, 7, 89, 23, 4, 67]

mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print(f"Menor: {menor} \nMayor: {mayor}")

## Simulador de login con intentos

usuario_correcto = "mario"
password_correcta = "python123"
intentos = 0

while intentos < 3 :
    intentos += 1
    usuario = input("Ingrese el usuario ")
    password = input("Ingrese la clave ")
    if usuario == usuario_correcto and password == password_correcta:
        print("Acceso Permitido")
    else:
        print("Clave o usuario equivocado")
else:
    print("Cuenta Bloqueada")

## Inventario simple

producto = "Laptop"
stock = 8
cantidad_solicitada = 3

if cantidad_solicitada <= stock :
    stock -= cantidad_solicitada
    print(f"Compra aceptada - Nuevo stock : {stock}")
else :
    print("Stock insuficiente")


## Calculadora con menú

while True:
    solicitud = input("Ingrese '1' = Sumar - '2' = Restar - '3' = Multiplicar - '4' Dividir - '5' Salir ")
    if solicitud == "1":
        num_a = float(input("Ingrese el primer numero "))
        num_b = float(input("Ingrese el segundo numero "))
        respuesta = num_a + num_b
    elif solicitud == "2":
        num_a = float(input("Ingrese el primer numero "))
        num_b = float(input("Ingrese el segundo numero "))
        respuesta = num_a  - num_b
    elif solicitud == "3":
        num_a = float(input("Ingrese el primer numero "))
        num_b = float(input("Ingrese el segundo numero "))
        respuesta = num_a  * num_b
    elif solicitud == "4":
        num_a = float(input("Ingrese el primer numero "))
        num_b = float(input("Ingrese el segundo numero "))
        if num_b == 0:
            respuesta = "Error"
        else:
            respuesta = num_a  / num_b
    elif solicitud == "5":
        break
    else:
        respuesta = "Solicitud Invalida"
    print(respuesta)

## Contar palabras en una frase

frase = "Estoy aprendiendo backend con Python"

frase_dividida = frase.split(" ")

print(f"La frase tiene un total de {len(frase_dividida)} palabras")


