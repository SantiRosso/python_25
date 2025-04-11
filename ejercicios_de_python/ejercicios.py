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
