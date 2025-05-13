# 2. Calcular la hora futura en un reloj de 12 horas 

hora_actual = int(input("Hora actual: "))
cantidad_horas = int(input("Cantidad de horas: "))

# Calculamos la nueva hora con módulo 12

hora_futura = (hora_actual + cantidad_horas) % 12

# Si da 0, significa que son las 12 en reloj de 12 horas

if hora_futura == 0:
    hora_futura = 12
print(f"En {cantidad_horas} horas, el reloj marcará las {hora_futura}")