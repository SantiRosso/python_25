# 1. Invertir un número

numero = int(input("Ingrese número: "))

# Convertimos a string, invertimos con slicing y volvemos a entero

numero_invertido = int(str(numero)[::-1])
print(numero_invertido)