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