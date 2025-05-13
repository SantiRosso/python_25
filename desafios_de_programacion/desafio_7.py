# 7. Secuencia de Collatz

numero = int(input("Ingrese un número: "))

print(numero, end=" ")

while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = numero * 3 + 1
    print(numero, end=" ")