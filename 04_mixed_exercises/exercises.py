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
    if letra.lower() in vocales:
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
        break
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

## Buscar una palabra

frase = "Python es excelente para backend"
palabra_buscada = "backend"

print("Palabra encontrada") if palabra_buscada in frase else print("Palabra no encontrada")

frase_auxiliar = frase.split()
palabra_encontrada = False

for f in frase_auxiliar:
    if f == palabra_buscada:
        palabra_encontrada = True
else: 
    print(palabra_encontrada)
    
## Limpieza básica de texto

texto = "   Python Backend   "

print(f"Texto Inicial: {texto} \nTexto Limpio: {texto.strip()} \nTexto Mayuscula: {texto.upper()} \nTexto miniscula: {texto.lower()}")

##  Separar números positivos y negativos

numeros = [4, -2, 7, -9, 0, 12, -1, 5]

positivos = []
negativos = []

for n in numeros:
    if n > 0 :
        positivos.append(n)
    else:
        negativos.append(n)

print(positivos, negativos)

## Separar pares e impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0 :
        pares.append(n)
    else:
        impares.append(n)

print(pares, impares)

## Sistema de ahorro con meta

meta = 200000
ahorro = 0

while ahorro < meta:
    ingreso = 0
    while ingreso <= 0 :
        ingreso = float(input("Ingrese un monto a ahorrar que sea mayor que cero"))
    ahorro += ingreso

print(f"Meta de ahorro alcanzada - Valor ahorrado {ahorro}")

## Clasificador de edades en lista

edades = [8, 15, 22, 34, 67, 3, 45, 90]
niños = 0
adolecentes = 0
adultos = 0 
adultos_mayores = 0

for e in edades:
    if e >= 0 and e <= 12:
        niños += 1
    elif e > 12 and e <= 17:
        adolecentes += 1
    elif e > 17 and e <= 59:
        adultos += 1
    elif e > 59:
        adultos_mayores += 1

print(f"Niños: {niños} \nAdolecentes: {adolecentes} \nAdultos: {adultos} \nAdultos Mayores: {adultos_mayores}")

## Carrito de compras simple

precios = [12000, 35000, 18000, 50000]

total = 0

for p in precios:
    total += p

if total >= 100000 :
    descuento = total * 10 / 100
    print(f"Total sin descuento: {total} - Descuento: {descuento} \nTotal a pagar {total - descuento}")
else:
    print(f"No tienes descuento, el total a pagar es de {total}")

## Detector de caracteres

texto = "Python 3.12 es genial!"

letras = "qwertyuiopasdfghjklñzxcvbnm"
numeros = "0123456789"

cantidad_letras = 0
cantidad_numeros = 0
cantidad_espacios = 0
cantidad_simbolos = 0

for t in texto :
    if t.lower() in letras :
        cantidad_letras += 1
    elif t in numeros :
        cantidad_numeros += 1
    elif t == " ":
        cantidad_espacios += 1
    else:
        cantidad_simbolos += 1

print(f"Letras: {cantidad_letras} - Numeros: {cantidad_numeros} - Espacios: {cantidad_espacios} - Simbolos: {cantidad_simbolos} ")

## Menú de tareas

tareas = []

while True:
    solicitud = input("Ingrese: '1' Agregar Tareas - '2' Ver tareas - '3' Eliminar ultima tarea - '4' Salir ")
    if solicitud == "1":
        tarea = input("Ingresa la nueva tarea ")
        tareas.append(tarea)
    elif solicitud == "2":
        print(tareas)
    elif solicitud == "3":
        if len(tareas) > 0:
            tareas.pop()
    elif solicitud == "4":
        break
    else:
        print("Opcion invalida")

## Mini evaluación de perfil backend

horas_python = 40
horas_sql = 10
horas_git = 8
proyectos = 1

horas_totales = horas_python + horas_sql + horas_git

print(f"Horas totales: {horas_totales} - Buen progreso inicial") if horas_totales >= 50 and proyectos >= 1 else print(f"Horas totales: {horas_totales} - Necesitas construir proyectos ")  if horas_totales >= 50 and proyectos <= 0 else print(f"Horas totales: {horas_totales} -Necesitas mas practica")
