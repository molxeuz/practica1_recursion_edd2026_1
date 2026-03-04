class Secuencia:
    def __init__(self, id, nombre, secuencia, riesgo):
        self.id = id
        self.nombre = nombre
        self.secuencia = secuencia
        self.riesgo = riesgo

# 1
def registrar(lista):
    opcion = input("\n¿Registrar nueva secuencia? (SI/NO): ")

    if opcion != "SI":
        return

    id = int(input("ID: "))
    nombre = input("Nombre: ")
    secuencia = input("Secuencia: ")
    riesgo = int(input("Nivel de riesgo: "))

    lista.append(Secuencia(id, nombre, secuencia, riesgo))

    return registrar(lista)

# 2
def contar_string(texto, patron):
    if len(texto) < len(patron):
        return 0

    if texto[:len(patron)] == patron:
        return 1 + contar_string(texto[1:], patron)
    else:
        return contar_string(texto[1:], patron)

# 3
def promedio(lista, i=0, suma=0):
    if i == len(lista):
        if len(lista) == 0:
            return 0
        return suma / len(lista)

    return promedio(lista, i + 1, suma + lista[i].riesgo)

# 4
def secuencia_larga(lista, i = 0, mayor = None):

    if len(lista) == 0:
        return None
    
    if i == len(lista):
        return mayor

    if mayor is None or len(lista[i].secuencia) > len(mayor.secuencia):
        mayor = lista[i]

    return secuencia_larga(lista, i+1, mayor)

# 5
def subcadenas_posibles(secuencia, i = 0, f = 0):

    if i == len(secuencia):
        return []
    
    if f == len(secuencia):
        return subcadenas_posibles(secuencia, i + 1, i + 1)
    
    return [secuencia[i:f+1]] + subcadenas_posibles(secuencia, i, f + 1)
    
# 6
def mas_nucleotidos(secuencia, i = 0):
    if i == len(secuencia):
        return 0
    
    if secuencia[i] == "A":
        return 1 + mas_nucleotidos(secuencia, i + 1)
    elif secuencia[i] == "T":
        return -1 + mas_nucleotidos(secuencia, i + 1)
    else:
        return mas_nucleotidos(secuencia, i + 1)

# 7
def mutacion_genetica(secuencia, i = 0):
    if i == len(secuencia):
        return ""
    
    if secuencia[i] == "A":
        nueva = "T"
    elif secuencia[i] == "T":
        nueva = "A"
    else:
        nueva = secuencia[i]

    return nueva + mutacion_genetica(secuencia, i + 1)

# Ejecucion:

if __name__ == "__main__":

    lista_secuencias = []

    # 1. Registrar secuencias
    registrar(lista_secuencias)

    print("\n1. Registros guardados:")
    for s in lista_secuencias:
        print("ID:", s.id)
        print("Nombre:", s.nombre)
        print("Secuencia:", s.secuencia)
        print("Riesgo:", s.riesgo)
        print()

    # 2. Contar patrón
    patron = "AG"
    print("2. Conteo patrón en cada secuencia:")
    for s in lista_secuencias:
        conteo = contar_string(s.secuencia, patron)
        print("Muestra", s.nombre, "->", conteo, "ocurrencias")

    print()

    # 3. Promedio riesgo
    print("3. Promedio de nivel de riesgo:")
    prom = promedio(lista_secuencias)
    print("Promedio:", prom)

    print()

    # 4. Secuencia más larga
    print("4. Secuencia más larga:")
    larga = secuencia_larga(lista_secuencias)

    if larga is not None:
        print("Nombre:", larga.nombre)
        print("Secuencia:", larga.secuencia)
    else:
        print("No hay secuencias registradas")

    print()

    # 5. Subcadenas
    print("5. Subcadenas posibles de cada secuencia:")
    for s in lista_secuencias:
        print("Muestra:", s.nombre)
        resultado = subcadenas_posibles(s.secuencia)
        print(resultado)

    print()

    # 6. Más A que T
    print("6. ¿Hay más A que T en cada secuencia?")
    for s in lista_secuencias:
        resultado = mas_nucleotidos(s.secuencia)
        if resultado > 0:
            print("La muestra", s.nombre, "tiene más A que T")
        else:
            print("La muestra", s.nombre, "NO tiene más A que T")

    print()

    # 7. Mutación genética
    print("7. Simulación de mutación genética:")
    for s in lista_secuencias:
        nueva = mutacion_genetica(s.secuencia)
        print("Muestra:", s.nombre)
        print("Original:", s.secuencia)
        print("Mutada:", nueva)
        print()