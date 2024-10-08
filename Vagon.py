class Vagon:
    def __init__(self, numero):
        self.numero = numero
        self.sillas = {}

    # esta funcion permite ocupar una silla con el numero que le otorgamos.
    def ocupar_silla(self, numero_silla, pasajero):
        if numero_silla not in self.sillas:
            self.sillas[numero_silla] = pasajero
        else:
            print(f"La silla {numero_silla} ya está ocupada.")

        # esta funcion permite bajar o liberar una silla con el numero que le otorgamos.
    def liberar_silla(self, numero_silla):
        if numero_silla in self.sillas:
            del self.sillas[numero_silla]
        else:
            print(f"La silla {numero_silla} no está ocupada.")

    # esta funcion permite que cuando piddamos una lista a la maquina, haga la respectiva lista con los pasajeros que hayan .
    def obtener_pasajeros(self):
        return list(self.sillas.values())
