class NodoADN:
    def __init__(self, id, nombre, secuencia, riesgo):
        self.id = id
        self.nombre = nombre
        self.secuencia = secuencia
        self.riesgo = riesgo
        self.siguiente = None
        
class ListaADN:
    def __init__(self):
        self.cabeza = None
        
        # 1. Registrar nuevas secuencias:
        
        def registrar(self, id, nombre, secuencia, riesgo):
        nuevo = Nodo(id, nombre, secuencia, riesgo)

            if self.cabeza is None: # si lista vacía
                self.cabeza = nuevo
            else:
                self._agregar(self.cabeza, nuevo)
    
        def _agregar(self, actual, nuevo):
            
            if actual.siguiente is None: # si es el último
                actual.siguiente = nuevo
            else:
                self._agregar(actual.siguiente, nuevo)
        
        # 2. Contar ocurrencias patron:
        
        
        
        # 3. Promedio de riesgo (recursion cola)
        
        
        
        # 4. Secuencia mas larga:
        
        def mas_larga(self):
            return self._mas_larga(self.cabeza)

        def _mas_larga(self, nodo):
            if nodo is None:
                return None
    
            if nodo.siguiente is None:
                return nodo
    
            resto = self._mas_larga(nodo.siguiente)
    
            if len(nodo.secuencia) > len(resto.secuencia):
                return nodo
            else:
                return resto
    
    
