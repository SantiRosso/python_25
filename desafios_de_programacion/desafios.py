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

# 10. Torre y Alfil. Función para determinar si un alfil o una torre capturan a la otra en un tablero de ajedrez.

def torre_y_alfil(fila_alfil, col_alfil, fila_torre, col_torre):
    # Verificar si el alfil captura (movimiento diagonal)
    if abs(fila_alfil - fila_torre) == abs(col_alfil - col_torre):
        return "Alfil captura"
    
    # Verificar si la torre captura (misma fila o misma columna)
    elif fila_alfil == fila_torre or col_alfil == col_torre:
        return "Torre captura"
    
    else:
        return "Ninguna captura"

# Ejemplos del ejercicio
print(torre_y_alfil(7, 6, 4, 3))  # Alfil captura
print(torre_y_alfil(3, 4, 7, 4))  # Torre captura
print(torre_y_alfil(3, 3, 8, 5))  # Ninguna captura

# 11. Piedra papel tijera.
def determinar_ganador(j1, j2):
    if j1 == j2:
        return 0  # Empate
    elif (j1 == "tijera" and j2 == "papel") or \
         (j1 == "papel" and j2 == "piedra") or \
         (j1 == "piedra" and j2 == "tijera"):
        return 1  # Gana jugador A
    else:
        return 2  # Gana jugador B

# Marcadores 
puntos_A = 0
puntos_B = 0

while puntos_A < 3 and puntos_B < 3:
    jugada_A = input("A: ").lower()
    jugada_B = input("B: ").lower()

    ganador = determinar_ganador(jugada_A, jugada_B)

    if ganador == 1:
        puntos_A += 1
    elif ganador == 2:
        puntos_B += 1

    print(f"{puntos_A} - {puntos_B}")

# Resultado final
if puntos_A == 3:
    print("A es el ganador")
else:
    print("B es el ganador")


# 12. Tenis. Simulación de un torneo de tenis con 8 jugadores.
# Paso 1: Cargar jugadores
jugadores = []
for i in range(8):
    nombre = input(f"Jugador {i+1}: ")
    jugadores.append(nombre)

ronda = 1

while len(jugadores) > 1:
    print(f"\nRonda {ronda}")
    ganadores = []

    for i in range(0, len(jugadores), 2):
        j1 = jugadores[i]
        j2 = jugadores[i+1]
        print(f"a. {j1} - b. {j2}")
        ganador = input("¿Quién gana (a/b)? ").lower()
        if ganador == "a":
            ganadores.append(j1)
        else:
            ganadores.append(j2)

    jugadores = ganadores
    ronda += 1

# Campeón
print(f"\nCampeón: {jugadores[0]}")

# 13. Cuántos países en común. Función para contar cuántos países tienen en común dos personas.
paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}

def cuantos_en_comun(a, b):
    return len(paises[a] & paises[b])  # Intersección de conjuntos

# 14. Horóscopo. Función para determinar el signo zodiacal de una persona según su fecha de nacimiento.
# Diccionario de signos y sus fechas de inicio y fin
signos = {
    'aries':      ((3, 21), (4, 20)),
    'tauro':      ((4, 21), (5, 21)),
    'geminis':    ((5, 22), (6, 21)),
    'cancer':     ((6, 22), (7, 22)),
    'leo':        ((7, 23), (8, 23)),
    'virgo':      ((8, 24), (9, 23)),
    'libra':      ((9, 24), (10, 23)),
    'escorpio':   ((10, 24), (11, 22)),
    'sagitario':  ((11, 23), (12, 21)),
    'capricornio':((12, 22), (1, 20)),
    'acuario':    ((1, 21), (2, 19)),
    'piscis':     ((2, 20), (3, 20)),
}

def determinar_signo(fecha_de_nacimiento):
    anio, mes, dia = fecha_de_nacimiento
    for signo, ((mes_inicio, dia_inicio), (mes_fin, dia_fin)) in signos.items():
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin) or (mes_inicio < mes_fin and mes > mes_inicio and mes < mes_fin) or (mes_inicio > mes_fin and (mes > mes_inicio or mes < mes_fin)):
            return signo
    return None  # Por si no encuentra (no debería pasar)

# Ejemplos del ejercicio
print(determinar_signo((1990, 5, 7)))   # tauro
print(determinar_signo((1904, 11, 24))) # sagitario
print(determinar_signo((1999, 12, 29))) # capricornio
print(determinar_signo((1999, 1, 11)))  # capricornio

# 15. Libros. Funciones para obtener información sobre libros y autores.

# Datos
libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
    ('Raw_input y Julieta', 'William Shakespeare', 1597),
    ('La tuplamorfosis', 'Franz Kafka', 1915),
]

autores = {
    'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
    'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
    'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
    'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),
}

# Funciones
def obtener_autor(titulo):
    for libro, autor, anio in libros:
        if libro == titulo:
            return autor
    return None

def obtener_idioma(titulo):
    autor = obtener_autor(titulo)
    if autor:
        return autores[autor][2]
    return None

def calcular_annos_antes_de_morir(titulo):
    autor = obtener_autor(titulo)
    if autor:
        anio_libro = next(anio for libro, autor_libro, anio in libros if libro == titulo)
        anio_muerte = autores[autor][1][0]
        return anio_muerte - anio_libro
    return None

titulo = input('Ingrese título del libro: ')
print('El libro fue escrito en', obtener_idioma(titulo))
print('por', obtener_autor(titulo))
print('El autor falleció', calcular_annos_antes_de_morir(titulo), 'años')
print('después de haber escrito el libro')

# 16. Código Morse. Funciones para codificar y decodificar texto a código Morse y viceversa.

# Diccionario de traducción
morse_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.', 
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---', 
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---', 
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-', 
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--', 
    'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-', 
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ''
}

# Invertimos el diccionario para decodificar Morse
inv_morse_dict = {v: k for k, v in morse_dict.items()}

def texto_a_morse(texto):
    texto = texto.upper()
    morse = ''
    for letra in texto:
        if letra != ' ':
            morse += morse_dict.get(letra, '') + ' '
        else:
            morse += '  '  # Dos espacios entre palabras
    return morse.strip()

def morse_a_texto(morse):
    palabras = morse.split('  ')  # Separar palabras
    texto = ''
    for palabra in palabras:
        letras = palabra.split()
        for letra in letras:
            texto += inv_morse_dict.get(letra, '')
        texto += ' '
    return texto.strip()

def detectar_tipo(texto):
    if all(c in ['.', '-', ' '] for c in texto):
        return 'morse'
    else:
        return 'texto'

# Programa principal
entrada = input("Ingrese texto o código Morse: ")

tipo = detectar_tipo(entrada)

if tipo == 'texto':
    print("Texto a Morse:", texto_a_morse(entrada))
else:
    print("Morse a Texto:", morse_a_texto(entrada))
