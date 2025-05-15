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