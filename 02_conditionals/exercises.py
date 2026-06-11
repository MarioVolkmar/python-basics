## Mayor de edad

edad = 20

if edad >= 18 :
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

## Número positivo, negativo o cero

numero = 5

if numero == 0:
    print("El numero es cero")
elif numero > 0:
    print("EL numero es positivo")
else:
    print("El numero es negativo")

## Par o impar

num = 5

if num % 2 == 0 :
    print("El numero es par")
else:
    print("El numero es impar")

## Nota aprobada o reprobada

nota = 3.5

if nota >= 3:
    print("Aprobado")
else: 
    print("Reprobado")

## Temperatura Ambiental

temperatura = 28

if temperatura < 15 :
    print("Hace frio")
elif temperatura >= 15 and temperatura <= 25:
    print("Es fresco")
else:
    print("Hace calor")

## Clasificación de nota

nota = 4.5

if nota >= 4.5:
    print("Excelente")
elif nota >=4 and nota <4.5:
    print("Muy bien")
elif nota >=3 and nota <4:
    print("Aprobado")
else:
    print("Reprobado")

## Día de la semana

semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

dia_semana  = 4

print(f"El dia de la semana que tiene como numero el {dia_semana} es {semana[dia_semana-1]}")

## Otra Opcion seria

dia_semana = 4

if dia_semana == 1:
    print("Lunes")
elif dia_semana == 2:
    print("Martes")
elif dia_semana == 3:
    print("Miercoles")
elif dia_semana == 4:
    print("Jueves")
elif dia_semana == 5:
    print("Viernes")
elif dia_semana == 6:
    print("Sabado")
elif dia_semana == 7:
    print("Domingo")

## Calculadora Basica

num_a = float(input("Ingrese el primer numero"))
num_b = float(input("Ingrese el segundo numero"))
operacion = input("Ingrese una se las siguientes operaciones -> suma - resta - multiplicar - dividir")

if operacion.lower() == "suma":
    print(f"El resultado es: {num_a + num_b}")
elif operacion.lower() == "resta":
    print(f"El resultado es: {num_a - num_b}")
elif operacion.lower() == "multiplicar":
    print(f"El resultado es: {num_a * num_b}")
elif operacion.lower() == "dividir":
    if num_b == 0:
        print("Indeterminado")
    else:
        print(f"El resultado es: {num_a / num_b}")
else:
    print("Operacion invalida")

## Clasificación por edad

edad = 23

if edad <0 :
    print("Edad invalida")
elif edad >= 0 and edad <=12:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolecente")
elif edad >= 18 and edad <= 59:
    print("Adulto")
else:
    print("Adulto Mayor")

## Semáforo

semaforo = "verde"

if semaforo.lower() == "verde":
    print("Avance")
elif semaforo.lower() == "amarillo":
    print("Precaucion")
elif semaforo.lower() == "rojo":
    print("Detenerse")
else:
    print("Color invalido")