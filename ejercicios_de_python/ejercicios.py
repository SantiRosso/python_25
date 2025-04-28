# OPERADORES

"""
Programa 1: Cálculo del área de un círculo
"""
import math

print("Programa 1: Cálculo del área de un círculo")

# Solicitar el radio al usuario
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área
area = math.pi * radio ** 2

# Mostrar el resultado
print(f"El área del círculo con radio {radio} es: {area:.2f}")

"""
Programa 2: Conversión de temperatura de Celsius a Fahrenheit
"""
print("\nPrograma 2: Conversión de temperatura de Celsius a Fahrenheit")

# Solicitar la temperatura en Celsius al usuario
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print(f"{celsius}°C es igual a {fahrenheit}°F")

"""
Programa 3: Cálculo de la hipotenusa de un triángulo rectángulo
"""
print("\nPrograma 3: Cálculo de la hipotenusa de un triángulo rectángulo")

# Solicitar los catetos al usuario
cateto_a = float(input("Ingrese la longitud del primer cateto: "))
cateto_b = float(input("Ingrese la longitud del segundo cateto: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

# Mostrar el resultado
print(f"La hipotenusa del triángulo rectángulo es: {hipotenusa:.2f}")

"""
Programa 4: Saludo personalizado con cálculo de edad
"""
import datetime

print("\nPrograma 4: Saludo personalizado con cálculo de edad")

# Solicitar nombre y año de nacimiento
nombre = input("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Obtener el año actual
año_actual = datetime.datetime.now().year

# Calcular la edad aproximada
edad = año_actual - año_nacimiento

# Mostrar el saludo personalizado
print(f"\n¡Hola {nombre}! Tienes aproximadamente {edad} años.")

# CONDICIONALES

# Ejercicio 1: Determinar si un número es par o impar

numero = int(input("Ingrese un número entero positivo: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicio 2: Verificar si un número es primo

numero = int(input("Ingrese un número entero positivo: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} NO es primo")

# Ejercicio 3: División segura (verificando denominador ≠ 0)

numerador = float(input("Ingrese el numerador: "))
denominador = float(input("Ingrese el denominador: "))

if denominador != 0:
    resultado = numerador / denominador
    print(f"El resultado de la división es: {resultado}")
else:
    print("Error: No se puede dividir por 0.")

# Desafíos:

# 1. Escribe un programa que solicite tres lados de un triángulo e indique si es
# equilátero, isósceles o escaleno.

lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")

# 2. Escribe un programa que solicite al usuario que ingrese una contraseña y confirme
#  la contraseña. El programa debe verificar si ambas contraseñas coinciden y no
#  están vacías.

contrasena1 = input("Ingrese una contraseña: ")
contrasena2 = input("Confirme la contraseña: ")

if contrasena1 and contrasena2 and contrasena1 == contrasena2:
    print("Las contraseñas coinciden")
else:
    print("Error: Las contraseñas no coinciden o están vacías")


# 3. Escribe un programa que solicite al usuario el precio y la cantidad de un producto.
#  Clasifique el producto como "caro" si el precio es mayor de $100 o si la cantidad es
#  menor que 10 y el precio es mayor de $50. De lo contrario, clasifíquelo como
#  "barato". Incluye condiciones para manejar valores falsos (0 o vacío).

precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))

if precio > 0 and cantidad > 0:
    if precio > 100 or (cantidad < 10 and precio > 50):
        print("El producto es caro")
    else:
        print("El producto es barato")
else:
    print("Error: El precio o la cantidad no pueden ser 0 ni negativos")


# 4. Escribe un programa que solicite al usuario su nombre, edad y número de teléfono.
#  Verifica que ninguno de estos datos esté vacío o sea un valor falso (por ejemplo, 0).

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
telefono = input("Ingrese su número de teléfono: ")

if nombre and edad.isdigit() and int(edad) > 0 and telefono:
    print("Datos ingresados correctamente")
else:
    print("Error: Verifique que ningún campo esté vacío o tenga un valor inválido")

# BUCLES

# 1. Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinar el número

import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        adivinado = True
        print(f"¡Correcto! El número era {numero_secreto}. Intentos: {intentos}")

# 2. Programa que sume todos los números de una lista

numeros = [1, 2, 3, 4, 5]
suma = 0

for numero in numeros:
    suma += numero

print(f"La suma de los números es: {suma}")

# 3. Programa que imprima el cuadrado de los números del 1 al 10

for numero in range(1, 11):
    print(f"El cuadrado de {numero} es {numero ** 2}")

# 4. Programa que cuente los caracteres de una cadena proporcionada por el usuario

texto = input("Introduce una cadena de texto: ")
contador = 0

for caracter in texto:
    contador += 1

print(f"La cantidad de caracteres es: {contador}")

# 5. Programa que cuente el número de vocales en una cadena de texto

texto = input("Introduce una cadena de texto: ").lower()
vocales = 'aeiou'
contador_vocales = 0

for letra in texto:
    if letra in vocales:
        contador_vocales += 1

print(f"El número de vocales es: {contador_vocales}")

# Desafíos: Estructura de datos:

# Lista inicial
amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']

# 1. Devuelve la posición (índice) del amigo "Matías"
indice_matias = amigos.index('Matías')
print(f"Índice de Matías: {indice_matias}")

# 2. Añade los amigos de la infancia "Ivana" y "Andrés" como otra lista
amigos_infancia = ['Ivana', 'Andrés']
amigos.extend(amigos_infancia)
print(f"Lista con amigos de la infancia: {amigos}")

# 3. Agrega un nuevo amigo "María" y devuelve el número de amigos
amigos.append('María')
cantidad_amigos = len(amigos)
print(f"Número de amigos después de agregar a María: {cantidad_amigos}")

# 4. Elimina el último elemento amigo y devuelve su nombre
amigo_eliminado = amigos.pop()
print(f"Amigo eliminado: {amigo_eliminado}")

# 5. Devuelve un arreglo ordenado alfabéticamente
amigos_ordenados = sorted(amigos)
print(f"Lista ordenada alfabéticamente: {amigos_ordenados}")

# Ejercicios extra

# 1. Lista desordenada ordenada ascendente y descendente

numeros = [5, 1, 9, 3, 7]
print("Lista original:", numeros)

# Orden ascendente
numeros_asc = sorted(numeros)
print("Orden ascendente:", numeros_asc)

# Orden descendente
numeros_desc = sorted(numeros, reverse=True)
print("Orden descendente:", numeros_desc)

# 2. Lista que cuenta las veces que aparece un número ingresado

numeros = [1, 2, 3, 4, 5, 3, 2, 3, 4]
num_usuario = int(input("Ingresa un número: "))

veces = numeros.count(num_usuario)
print(f"El número {num_usuario} aparece {veces} veces en la lista.")

# 3. Tupla con tres colores favoritos e imprimir el segundo

colores = ('azul', 'rojo', 'verde')
print(f"El segundo color es: {colores[1]}")

# 4. Tupla de números y verificar si un número existe

numeros = (10, 20, 30, 40, 50)
num_usuario = int(input("Ingresa un número: "))

if num_usuario in numeros:
    print("El número existe en la tupla.")
else:
    print("El número NO existe en la tupla.")

# 5. Programa para administrar el inventario de una tienda

inventario = {}

def mostrar_inventario():
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

def agregar_producto(producto, cantidad):
    inventario[producto] = cantidad

def actualizar_producto(producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        print("El producto no existe.")

# Ejemplo de uso:
agregar_producto('manzanas', 10)
agregar_producto('bananas', 5)
actualizar_producto('manzanas', 5)
mostrar_inventario()

# 6. Programa para registrar calificaciones de estudiantes

calificaciones = {}

def agregar_estudiante(nombre, notas):
    calificaciones[nombre] = notas

def actualizar_calificaciones(nombre, notas):
    if nombre in calificaciones:
        calificaciones[nombre].extend(notas)
    else:
        print("Estudiante no encontrado.")

def promedio_estudiante(nombre):
    if nombre in calificaciones:
        promedio = sum(calificaciones[nombre]) / len(calificaciones[nombre])
        print(f"El promedio de {nombre} es {promedio:.2f}")
    else:
        print("Estudiante no encontrado.")

# Ejemplo de uso:
agregar_estudiante('Juan', [8, 9, 10])
actualizar_calificaciones('Juan', [7])
promedio_estudiante('Juan')

# FUNCIONES

# 1. Función que recibe un nombre y devuelve un saludo personalizado
def saludar_usuario(nombre):
    """Devuelve un saludo personalizado."""
    if not nombre:
        return "Hola, desconocido."
    return f"¡Hola, {nombre}! Bienvenido."

# Ejemplo de uso
#print(saludar_usuario("Ana"))

# 2. Función que calcule el factorial de un número
def calcular_factorial(numero):
    """Calcula el factorial de un número entero no negativo."""
    if numero < 0:
        return "Error: el factorial no está definido para números negativos."
    
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Ejemplo de uso
#print(calcular_factorial(5))  # Resultado: 120

# 3. Función que recibe una lista de números y devuelve el promedio
def calcular_promedio(lista_numeros):
    """Calcula el promedio de una lista de números."""
    if not lista_numeros:
        return "Error: la lista está vacía."
    
    suma = sum(lista_numeros)
    cantidad = len(lista_numeros)
    return suma / cantidad

# Ejemplo de uso
#print(calcular_promedio([7, 8, 9]))  # Resultado: 8.0

# 4. Funciones para conversión entre número entero y binario

# 4. 1. Entero a binario

def convertir_a_binario(numero):
    """Convierte un número entero no negativo a binario."""
    if numero < 0:
        return "Error: solo se aceptan números enteros no negativos."
    return bin(numero)[2:]

# Ejemplo de uso
#print(convertir_a_binario(10))  # Resultado: '1010'

#4. 2. Binario a entero

def convertir_a_entero(binario):
    """Convierte una cadena binaria a su valor entero."""
    try:
        return int(binario, 2)
    except ValueError:
        return "Error: valor binario inválido."

# Ejemplo de uso
#print(convertir_a_entero('1010'))  # Resultado: 10
