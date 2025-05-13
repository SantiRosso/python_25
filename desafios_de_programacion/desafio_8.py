# 8. 

# Precios de los productos
productos = {
    'A': 270,
    'B': 340,
    'C': 390
}

# Monedas aceptadas
monedas_validas = [10, 50, 100]

# Función para dar el vuelto en monedas
def dar_vuelto(vuelto):
    print("Vuelto:")
    for moneda in sorted(monedas_validas, reverse=True):
        while vuelto >= moneda:
            print(moneda)
            vuelto -= moneda

# Mostrar productos y pedir elección
print("Productos disponibles:")
for nombre, precio in productos.items():
    print(f"Producto {nombre}: ${precio}")

producto_elegido = input("Elegí un producto (A, B o C): ").upper()

# Validar producto elegido
if producto_elegido in productos:
    precio = productos[producto_elegido]
    print(f"Precio del producto {producto_elegido}: ${precio}")
    
    total_ingresado = 0

    # Ingreso de monedas
    while total_ingresado < precio:
        try:
            moneda = int(input("Ingresá una moneda ($10, $50, $100): "))
            if moneda in monedas_validas:
                total_ingresado += moneda
                print(f"Total ingresado: ${total_ingresado}")
            else:
                print("Moneda no válida.")
        except ValueError:
            print("Por favor ingresá un número válido.")

    # Calcular y dar vuelto si hay
    if total_ingresado > precio:
        vuelto = total_ingresado - precio
        dar_vuelto(vuelto)
    else:
        print("No hay vuelto. Gracias por tu compra.")

else:
    print("Producto no válido.")