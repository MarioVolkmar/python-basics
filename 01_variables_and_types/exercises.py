########################## 1 Datos personales

nombre = "Mario"
edad = 32
ciudad = "Medellin"
estatura = 1.78
estudio_python = True
print(f"Hola mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad} y amo PY {'SI' if estudio_python else 'NO'}")

########################## 2 Tipos de datos básicos

print(type(nombre),type(edad),type(estatura),type(estudio_python))

########################## 3 Suma de dos números

num_a = 15
num_b = 49

print(f"La suma es de {num_a + num_b}")

########################## 4 Operaciones básicas, 5 División entera y módulo

x = 20
y = 6

print(f"Suma = {x + y}")
print(f"Resta = {x - y}")
print(f"Multiplicacion = {x * y}")
print(f"Division = {x / y}")
print(f"Division Entera = {x // y}")
print(f"Modulo/Residuo = {x % y}")

########################## 6 Área de un rectángulo, 7 Área de un círculo

base = 20
altura = 35

print(f"El area del rectangulo de base {base} y altura {altura} es de {base * altura}")

radio = 6
pi = 3.1416

print(f"El area del circulo de radio {radio}  es de {pi * radio **2}")

########################## 8 Conversión de string a entero

edad_texto = input("Ingresa tu edad actual ")

print(f"En 5 años tendras {int(edad_texto) + 5} años")

########################## 9 Conversión de string a decimal

precio = input("Ingresa el precio del bien ")
cantidad = input("Ingrese la cantidad comprada ")

print(f"El total a pagar es de {float(precio) * int(cantidad)}")

########################## 10 Concatenación de strings

nom = "Mario"
apellido = "Medina Volkmar"
nombre_completo = f"{nom} {apellido}"
nombre_completo2 = nom + ' ' + apellido

print(f"Mi nombre completo es {nombre_completo}")

########################## 11 Cálculo de edad aproximada en días

edad = 32

print(f"Aproximadamente has vivido un total de {edad * 365} dias")

########################## 12 Precio con IVA

precio = 15000
iva = 19

print(f"El impuesto a cancelar es de {precio * iva / 100} y el total a pagar es de {precio * (iva + 100) / 100}")

########################## 13 Descuento de producto

precio = 255054
descuento = 16

print(f"El descuento es de {precio * descuento / 100} y el monto a pagar es de {precio * (100 - descuento) / 100}")

########################## 14 Promedio de notas

nota1 = 4.2
nota2 = 3.8
nota3 = 4.5

print(f"El promedio es {((nota1 + nota2 + nota3) / 3):.2f}")

########################## 15 Intercambio de variables

a = 10
b = 20
tem = a
a = b
b = tem

print(a,b)

########################## 16 Intercambio rápido estilo Python

a = 10
b = 20
a, b = b, a

print(a,b)

########################## 17 Booleanos

is_active = True
is_admin = False

print(f"Usuario activo: {is_active} \nUsuario Administrador: {is_admin}")

########################## 18 Largo de un texto

mensaje = "Estoy aprendiendo Python"

print(f"El mensaje tiene {len(mensaje)} caracteres")

########################## 19 Mayúsculas y minúsculas

nombre = "mario volkmar"

print(nombre.upper())
print(nombre.title())
print(nombre.lower())

########################## 20 Mini ficha técnica personal

nombre = "Mario"
edad = 32
profesion_anterior = "Ingeniero Mecánico"
objetivo = "Backend Developer Junior"
horas_semana = 40
lenguaje = "Python"

print(
        f'Perfil Estudiante \nNombre: {nombre} \nEdad: {edad} \nProfesion anterior: {profesion_anterior} \nObjetivo: {objetivo} \nHoras de estudio semanal: {horas_semana} \nLenguaje Principal: {lenguaje} '
    )




