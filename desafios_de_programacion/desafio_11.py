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