# 5. Verificar si un año es bisiesto

año = int(input("Ingrese el año a evaluar: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} NO es bisiesto")