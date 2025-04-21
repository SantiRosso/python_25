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

# 8. 

# Precios de los productos
productos = {
    'A': 270,
    'B': 340,
    'C': 390
}

# Monedas aceptadas
monedas_validas = [10, 50, 100]

# Función para dar el vuelto en monedas
def dar_vuelto(vuelto):
    print("Vuelto:")
    for moneda in sorted(monedas_validas, reverse=True):
        while vuelto >= moneda:
            print(moneda)
            vuelto -= moneda

# Mostrar productos y pedir elección
print("Productos disponibles:")
for nombre, precio in productos.items():
    print(f"Producto {nombre}: ${precio}")

producto_elegido = input("Elegí un producto (A, B o C): ").upper()

# Validar producto elegido
if producto_elegido in productos:
    precio = productos[producto_elegido]
    print(f"Precio del producto {producto_elegido}: ${precio}")
    
    total_ingresado = 0

    # Ingreso de monedas
    while total_ingresado < precio:
        try:
            moneda = int(input("Ingresá una moneda ($10, $50, $100): "))
            if moneda in monedas_validas:
                total_ingresado += moneda
                print(f"Total ingresado: ${total_ingresado}")
            else:
                print("Moneda no válida.")
        except ValueError:
            print("Por favor ingresá un número válido.")

    # Calcular y dar vuelto si hay
    if total_ingresado > precio:
        vuelto = total_ingresado - precio
        dar_vuelto(vuelto)
    else:
        print("No hay vuelto. Gracias por tu compra.")

else:
    print("Producto no válido.")

# 9. Es anagrama. Función para verificar si dos palabras son anagramas

def es_anagrama(palabra1, palabra2):
    # Convertimos a minúsculas para evitar errores por mayúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Si son exactamente iguales, no es anagrama
    if palabra1 == palabra2:
        return False

    # Ordenamos las letras y comparamos
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
print(es_anagrama("Sergio", "Riesgo"))  # True
print(es_anagrama("Hola", "hola"))      # False
print(es_anagrama("Amor", "Roma"))      # True
