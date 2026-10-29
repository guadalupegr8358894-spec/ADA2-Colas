from collections import deque

class Cola:
    """Implementación de la estructura de datos Cola (Queue) utilizando deque."""
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

    def encolar(self, item):
        """Agrega un elemento al final de la cola."""
        self.items.append(item)

    def desencolar(self):
        """Remueve y devuelve el primer elemento de la cola."""
        if not self.esta_vacia():
            return self.items.popleft()
        raise IndexError("La cola está vacía")

    def __str__(self):
        """Permite visualizar el contenido de la cola."""
        return str(list(self.items))


def sumar_colas(cola_a, cola_b):
    """
    Recibe dos Colas con números enteros y devuelve una nueva Cola 
    con sus elementos sumados uno a uno.
    """
    resultado = Cola()
    aux_a = Cola()
    aux_b = Cola()
    
    # Recorremos ambas colas mientras tengan elementos
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        val_a = cola_a.desencolar()
        val_b = cola_b.desencolar()
        
        # Sumamos los elementos correspondientes y los guardamos en la cola resultado
        resultado.encolar(val_a + val_b)
        
        # Guardamos en colas auxiliares para restaurar las originales después
        aux_a.encolar(val_a)
        aux_b.encolar(val_b)
        
    # Restaurar los elementos originales en cola_a y cola_b
    while not aux_a.esta_vacia():
        cola_a.encolar(aux_a.desencolar())
    while not aux_b.esta_vacia():
        cola_b.encolar(aux_b.desencolar())
        
    return resultado


# --- Bloque de prueba con los datos del ejemplo ---
if __name__ == "__main__":
    # Inicialización de la Cola A
    cola_a = Cola()
    for val in [3, 4, 2, 8, 12]:
        cola_a.encolar(val)

    # Inicialización de la Cola B
    cola_b = Cola()
    for val in [6, 2, 9, 11, 3]:
        cola_b.encolar(val)

    print("--- DATOS DE ENTRADA ---")
    print(f"Cola A:        {cola_a}")
    print(f"Cola B:        {cola_b}")

    # Ejecución de la función
    cola_resultado = sumar_colas(cola_a, cola_b)

    print("\n--- RESULTADO ---")
    print(f"Cola Resultado: {cola_resultado}")