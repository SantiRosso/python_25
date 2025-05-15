# 13. Cuántos países en común. Función para contar cuántos países tienen en común dos personas.
paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}

def cuantos_en_comun(a, b):
    return len(paises[a] & paises[b])  # Intersección de conjuntos