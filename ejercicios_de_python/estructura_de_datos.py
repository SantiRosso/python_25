# Desafíos: Estructura de datos:

# Lista inicial
amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']

# 1. Devuelve la posición (índice) del amigo "Matías"
indice_matias = amigos.index('Matías')
print(f"Índice de Matías: {indice_matias}")

# 2. Añade los amigos de la infancia "Ivana" y "Andrés" como otra lista
amigos_infancia = ['Ivana', 'Andrés']
amigos.extend(amigos_infancia)
print(f"Lista con amigos de la infancia: {amigos}")

# 3. Agrega un nuevo amigo "María" y devuelve el número de amigos
amigos.append('María')
cantidad_amigos = len(amigos)
print(f"Número de amigos después de agregar a María: {cantidad_amigos}")

# 4. Elimina el último elemento amigo y devuelve su nombre
amigo_eliminado = amigos.pop()
print(f"Amigo eliminado: {amigo_eliminado}")

# 5. Devuelve un arreglo ordenado alfabéticamente
amigos_ordenados = sorted(amigos)
print(f"Lista ordenada alfabéticamente: {amigos_ordenados}")