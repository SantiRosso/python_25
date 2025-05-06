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