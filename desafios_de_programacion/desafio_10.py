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