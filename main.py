class Nodo:
    def __init__(self, id, nombre, secuencia, riesgo):
        self.id = id
        self.nombre = nombre
        self.secuencia = secuencia
        self.riesgo = riesgo
        self.sig = None   # apunta al siguiente nodo
        
class ListaADN:
    def __init__(self):
        self.cabeza = None
        
    # 1. Registrar nuevas secuencias:
    
    def registrar(self, id, nombre, secuencia, riesgo):
        nuevo = Nodo(id, nombre, secuencia, riesgo)

        if self.cabeza is None:        # si está vacía
            self.cabeza = nuevo
        else:
            self._agregar(self.cabeza, nuevo)

    def _agregar(self, actual, nuevo):
        if actual.sig is None:         # si es el último
            actual.sig = nuevo
        else:
            self._agregar(actual.sig, nuevo)
    
    # 2. Contar ocurrencias patron:
    
    def contar_patron(self, patron):
        self._contar_lista(self.cabeza, patron)

    def _contar_lista(self, nodo, patron):
        if nodo is None:
            return

        print(nodo.nombre, "->",
              self._contar_string(nodo.secuencia, patron))

        self._contar_lista(nodo.sig, patron)

    def _contar_string(self, texto, patron):
        if len(texto) < len(patron):   # caso base
            return 0

        if texto[:len(patron)] == patron:
            return 1 + self._contar_string(texto[1:], patron)
        else:
            return self._contar_string(texto[1:], patron)

    # 3. Promedio de riesgo (recursion cola):
    
    def promedio(self):
        suma, cant = self._promedio(self.cabeza, 0, 0)

        if cant == 0:
            return 0
        return suma / cant

    def _promedio(self, nodo, suma, cant):
        if nodo is None:
            return suma, cant

        # llamada es lo último → cola
        return self._promedio(
            nodo.sig,
            suma + nodo.riesgo,
            cant + 1
        )
    
    # 4. Secuencia mas larga:
    
    def mas_larga(self):
        return self._mas_larga(self.cabeza)

    def _mas_larga(self, nodo):
        if nodo is None:
            return None

        if nodo.sig is None:
            return nodo

        resto = self._mas_larga(nodo.sig)

        if len(nodo.secuencia) > len(resto.secuencia):
            return nodo
        else:
            return resto

    # 5 Subcadenas:

    def subcadenas(self, texto):
        resultado = []
        self._inicio(texto, 0, resultado)
        return resultado

    def _inicio(self, texto, i, lista):
        if i >= len(texto):
            return

        self._fin(texto, i, i + 1, lista)
        self._inicio(texto, i + 1, lista)

    def _fin(self, texto, i, j, lista):
        if j > len(texto):
            return

        lista.append(texto[i:j])
        self._fin(texto, i, j + 1, lista)
        
    # 6 Mas A que T (Recursion cola):

    def mas_A_que_T(self, texto):
        return self._contar_AT(texto, 0, 0)

    def _contar_AT(self, texto, A, T):
        if texto == "":
            return A > T

        if texto[0] == "A":
            return self._contar_AT(texto[1:], A + 1, T)

        if texto[0] == "T":
            return self._contar_AT(texto[1:], A, T + 1)

        return self._contar_AT(texto[1:], A, T) 

    # 7 Mutacion genetica:

    def mutar(self, texto):
        if texto == "":
            return ""

        if texto[0] == "A":
            letra = "T"
        elif texto[0] == "T":
            letra = "A"
        else:
            letra = texto[0]

        return letra + self.mutar(texto[1:])

# Pruebas:

if __name__ == "__main__":

    lista = ListaADN()

    # 1
    lista.registrar(1, "M1", "ATGATAT", 5)
    lista.registrar(2, "M2", "TTGCA", 8)
    lista.registrar(3, "M3", "ATAT", 3)

    # 2
    print("\n2. Patrón AT:")
    lista.contar_patron("AT")

    # 3
    print("\n3. Promedio:")
    print(lista.promedio())

    # 4
    print("\n4. Más larga:")
    print(lista.mas_larga().secuencia)

    # 5
    print("\n5. Subcadenas ABC:")
    print(lista.subcadenas("ABC"))

    # 6
    print("\n6. Mas A que T:")
    print(lista.mas_A_que_T("ATGATA"))

    # 7
    print("\n7. Mutación:")
    print(lista.mutar("ATCGTA"))