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