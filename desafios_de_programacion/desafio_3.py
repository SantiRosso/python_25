# 3. Determinar si un número es primo

numero = int(input("Ingrese un número: "))

if numero < 2:
    print(f"El número {numero} no es primo")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")