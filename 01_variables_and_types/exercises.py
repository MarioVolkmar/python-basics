########################## 1

nombre = "Mario"
edad = 32
ciudad = "Medellin"
estatura = 1.78
estudio_python = True
print(f"Hola mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad} y amo PY {'SI' if estudio_python else 'NO'}")

########################## 2

print(type(nombre),type(edad),type(estatura),type(estudio_python))

########################## 3

num_a = 15
num_b = 49

print(f"La suma es de {num_a + num_b}")

########################## 4, 5

x = 20
y = 6

print(f"Suma = {x + y}")
print(f"Resta = {x - y}")
print(f"Multiplicacion = {x * y}")
print(f"Division = {x / y}")
print(f"Division Entera = {x // y}")
print(f"Modulo/Residuo = {x % y}")

########################## 6, 7

base = 20
altura = 35

print(f"El area del rectangulo de base {base} y altura {altura} es de {base * altura}")

radio = 6
pi = 3.1416

print(f"El area del circulo de radio {radio}  es de {pi * radio **2}")

########################## 8

edad_texto = input("Ingresa tu edad actual ")

print(f"En 5 años tendras {int(edad_texto) + 5} años")

########################## 9

precio = input("Ingresa el precio del bien ")
cantidad = input("Ingrese la cantidad comprada ")

print(f"El total a pagar es de {float(precio) * int(cantidad)}")

########################## 10

nom = "Mario"
apellido = "Medina Volkmar"
nombre_completo = f"{nom} {apellido}"

print(f"Mi nombre completo es {nombre_completo}")





