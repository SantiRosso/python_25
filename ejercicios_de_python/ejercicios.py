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
