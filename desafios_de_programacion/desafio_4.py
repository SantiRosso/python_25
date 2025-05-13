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