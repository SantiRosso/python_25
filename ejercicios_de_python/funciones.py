# FUNCIONES

# 1. Función que recibe un nombre y devuelve un saludo personalizado
def saludar_usuario(nombre):
    """Devuelve un saludo personalizado."""
    if not nombre:
        return "Hola, desconocido."
    return f"¡Hola, {nombre}! Bienvenido."

# Ejemplo de uso
#print(saludar_usuario("Ana"))

# 2. Función que calcule el factorial de un número
def calcular_factorial(numero):
    """Calcula el factorial de un número entero no negativo."""
    if numero < 0:
        return "Error: el factorial no está definido para números negativos."
    
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Ejemplo de uso
#print(calcular_factorial(5))  # Resultado: 120

# 3. Función que recibe una lista de números y devuelve el promedio
def calcular_promedio(lista_numeros):
    """Calcula el promedio de una lista de números."""
    if not lista_numeros:
        return "Error: la lista está vacía."
    
    suma = sum(lista_numeros)
    cantidad = len(lista_numeros)
    return suma / cantidad

# Ejemplo de uso
#print(calcular_promedio([7, 8, 9]))  # Resultado: 8.0

# 4. Funciones para conversión entre número entero y binario

# 4. 1. Entero a binario

def convertir_a_binario(numero):
    """Convierte un número entero no negativo a binario."""
    if numero < 0:
        return "Error: solo se aceptan números enteros no negativos."
    return bin(numero)[2:]

# Ejemplo de uso
#print(convertir_a_binario(10))  # Resultado: '1010'

#4. 2. Binario a entero

def convertir_a_entero(binario):
    """Convierte una cadena binaria a su valor entero."""
    try:
        return int(binario, 2)
    except ValueError:
        return "Error: valor binario inválido."

# Ejemplo de uso
#print(convertir_a_entero('1010'))  # Resultado: 10