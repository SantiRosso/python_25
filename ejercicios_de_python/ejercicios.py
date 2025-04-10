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