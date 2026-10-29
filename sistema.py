class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0


# Colas independientes para cada servicio
colas = {}
contadores = {}


def obtener_cola(servicio):
    if servicio not in colas:
        colas[servicio] = Cola()
        contadores[servicio] = 0
    return colas[servicio]


print("SISTEMA DE ATENCION - COMPANIA DE SEGUROS")
print("C seguido del numero de servicio: llega un cliente")
print("A seguido del numero de servicio: atender un cliente")
print("S: salir del sistema")

while True:
    comando = input("\nIngrese un comando: ").strip().upper()

    if comando == "S":
        print("Sistema finalizado.")
        break

    elif len(comando) > 1 and comando[0] in ("C", "A"):
        try:
            servicio = int(comando[1:])

            if servicio <= 0:
                print("El numero de servicio debe ser positivo.")
                continue

        except ValueError:
            print("Comando invalido. Ejemplos: C1, A1 o S.")
            continue

        cola = obtener_cola(servicio)

        if comando[0] == "C":
            contadores[servicio] += 1
            numero = contadores[servicio]
            cola.encolar(numero)

            print(
                f"Cliente registrado. "
                f"Servicio {servicio}, turno {numero}"
            )

        elif comando[0] == "A":
            numero = cola.desencolar()

            if numero is None:
                print(f"No hay clientes en el servicio {servicio}.")
            else:
                print(
                    f"Atendiendo servicio {servicio}, "
                    f"numero de atencion {numero}"
                )

    else:
        print("Comando invalido. Use C1, A1 o S.")
