# 6. Imprimir triángulo de números
 
renglones = int(input("Ingrese cantidad de renglones: "))

for i in range(1, renglones + 1):
    linea = []
    for j in range(i, 0, -1):
        linea.append(str(j * 2))
    print(" ".join(linea))