# 1. Invertir un número

numero = int(input("Ingrese número: "))

# Convertimos a string, invertimos con slicing y volvemos a entero

numero_invertido = int(str(numero)[::-1])
print(numero_invertido)

# 2. Calcular la hora futura en un reloj de 12 horas 

hora_actual = int(input("Hora actual: "))
cantidad_horas = int(input("Cantidad de horas: "))

# Calculamos la nueva hora con módulo 12

hora_futura = (hora_actual + cantidad_horas) % 12

# Si da 0, significa que son las 12 en reloj de 12 horas

if hora_futura == 0:
    hora_futura = 12
print(f"En {cantidad_horas} horas, el reloj marcará las {hora_futura}")

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

# 4. Calcular el tiempo total de un viaje

total_minutos = 0

while True:
    tramo = int(input("Duración tramo (en minutos): "))
    if tramo == 0:
        break
    total_minutos += tramo

horas = total_minutos // 60
minutos = total_minutos % 60

print(f"Tiempo total de viaje: {horas}:{minutos:02d} horas")

# 5. Verificar si un año es bisiesto

año = int(input("Ingrese el año a evaluar: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} NO es bisiesto")

# 6. Imprimir triángulo de números
 
renglones = int(input("Ingrese cantidad de renglones: "))

for i in range(1, renglones + 1):
    linea = []
    for j in range(i, 0, -1):
        linea.append(str(j * 2))
    print(" ".join(linea))

# 7. Secuencia de Collatz

numero = int(input("Ingrese un número: "))

print(numero, end=" ")

while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = numero * 3 + 1
    print(numero, end=" ")
