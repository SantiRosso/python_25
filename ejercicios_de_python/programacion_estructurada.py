# 1. Menú de Inventario de Productos

def menu_inventario():
    inventario = {}

    while True:
        print("\n--- Menú Inventario ---")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Buscar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            inventario[producto] = cantidad
        elif opcion == "2":
            print("Inventario:", inventario)
        elif opcion == "3":
            producto = input("Producto a buscar: ")
            if producto in inventario:
                print(f"{producto}: {inventario[producto]} unidades")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            producto = input("Producto a eliminar: ")
            if producto in inventario:
                del inventario[producto]
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

#menu_inventario()

# 2. Menú de Gestión de Contactos

def menu_contactos():
    contactos = {}

    while True:
        print("\n--- Menú Contactos ---")
        print("1. Agregar Contacto")
        print("2. Eliminar Contacto")
        print("3. Mostrar Contactos")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono: ")
            contactos[nombre] = telefono
        elif opcion == "2":
            nombre = input("Nombre del contacto a eliminar: ")
            if nombre in contactos:
                del contactos[nombre]
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")
        elif opcion == "3":
            print("Lista de contactos:", contactos)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

#menu_contactos()

# 3. Menú de Gestión de Usuarios y Contraseñas

def menu_usuarios():
    usuarios = {}

    while True:
        print("\n--- Menú Usuarios ---")
        print("1. Agregar Usuario")
        print("2. Eliminar Usuario")
        print("3. Mostrar Usuarios")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            usuarios[usuario] = contraseña
        elif opcion == "2":
            usuario = input("Usuario a eliminar: ")
            if usuario in usuarios:
                del usuarios[usuario]
                print("Usuario eliminado.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "3":
            print("Usuarios registrados:", list(usuarios.keys()))
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

#menu_usuarios()

# 4. Menú de Gestión de Tareas

def menu_tareas():
    tareas = []

    while True:
        print("\n--- Menú Tareas ---")
        print("1. Agregar Tarea")
        print("2. Marcar Tarea como Completada")
        print("3. Mostrar Tareas Pendientes")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tarea = input("Descripción de la tarea: ")
            tareas.append({'tarea': tarea, 'completada': False})
        elif opcion == "2":
            for i, t in enumerate(tareas):
                if not t['completada']:
                    print(f"{i}. {t['tarea']}")
            indice = int(input("Índice de tarea a completar: "))
            if 0 <= indice < len(tareas):
                tareas[indice]['completada'] = True
                print("Tarea marcada como completada.")
            else:
                print("Índice inválido.")
        elif opcion == "3":
            for t in tareas:
                if not t['completada']:
                    print("-", t['tarea'])
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

#menu_tareas()

# 5. Programa tipo Cajero Automático

def menu_cajero():
    usuario = "admin"
    contraseña = "1234"
    saldo = 1000

    usuario_input = input("Ingrese usuario: ")
    contraseña_input = input("Ingrese contraseña: ")

    if usuario_input == usuario and contraseña_input == contraseña:
        print("Inicio de sesión exitoso.")
        
        while True:
            print("\n--- Menú Cajero ---")
            print("1. Extracción")
            print("2. Depósito")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                monto = float(input("Ingrese monto a extraer: "))
                if monto <= saldo:
                    saldo -= monto
                    print(f"Extracción exitosa. Saldo actual: ${saldo:.2f}")
                else:
                    print("Saldo insuficiente.")
            elif opcion == "2":
                monto = float(input("Ingrese monto a depositar: "))
                saldo += monto
                print(f"Depósito exitoso. Saldo actual: ${saldo:.2f}")
            elif opcion == "3":
                print("Saliendo del cajero...")
                break
            else:
                print("Opción no válida.")
    else:
        print("Credenciales incorrectas.")

#menu_cajero()
