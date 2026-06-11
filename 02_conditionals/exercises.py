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

num_a = float(input("Ingrese el primer numero "))
num_b = float(input("Ingrese el segundo numero "))
operacion = input("Ingrese una se las siguientes operaciones -> suma - resta - multiplicar - dividir ")

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

## Login básico

usuario = "mario"
password = "1234"

print("Acceso concedido ") if usuario == "mario" and password == "1234" else print("Acceso denegado")

## Acceso con rol

usuario_activo = True
rol = "admin"

if usuario_activo and rol == "admin" :
    print("Puede ingresar al panel")
elif usuario_activo :
    print("Acceso Limitado")
elif not usuario_activo :
    print("Usuario Inactivo")

## Descuento por compra

compra = 25000
cliente_frecuente = True

if cliente_frecuente and compra >= 20000:
    print("Tiene descuento")
else:
    print("No tiene descuento")

## Validar rango de nota

nota = 5

if nota >= 0 and nota <= 5:
    print("Nota valida")
else:
    print("Nota invalida")

## Puede conducir

edad = 20
tiene_licencia = True

if tiene_licencia and edad >= 18:
    print("Puede conducir")
elif edad >= 18 :
    print("Necesitas la licencia de conduccion")
else:
    print("No puedes conducir siendo menor de edad")

## Validación de contraseña

password = "python123"

if len(password) >= 8:
    print("Contraseña Valida")
else:
    print("Contraseña demasiado corta")

## Evaluar salario

salario = 400000

if salario < 130000:
    print("Salario bajo")
elif salario >= 130000 and salario < 3000000:
    print("Salario Medio")
else:
    print("Salario Alto")

## Sistema de envío

total_compra = 120000
ciudad = "Medellin"

if total_compra >= 10000 and ciudad == "Medellin":
    print("Envio Gratis")
elif total_compra >= 10000:
    print("Envio con descuento")
else :
    print("Envio normal")

## Nivel de programador

horas_estudio = 80

if horas_estudio < 50:
    print("Principiante inicial")
elif horas_estudio >= 50 and horas_estudio <= 200:
    print("Principiante en progreso")
elif horas_estudio > 200 and horas_estudio <= 500:
    print("Nivel Basico")
else:
    print("Nivel Intermedio")

## Evaluador de perfil backend junior

sabe_python = True
sabe_sql = False
sabe_git = True
horas_estudio = 40

if sabe_python and sabe_git and horas_estudio >= 40 :
    print("Buen inicio")
elif sabe_python and not sabe_git:
    print("Debe mejorar git")
elif not sabe_python:
    print("Debe aprender python")
elif sabe_python and sabe_git and horas_estudio < 40:
    print("Debe practicar mas")