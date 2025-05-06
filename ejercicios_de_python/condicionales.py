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