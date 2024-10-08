class Tren:
    def __init__(self, paradas):
        self.vagones = []
        self.paradas = paradas
        self.personas_subidas = 0
        self.personas_bajadas = 0

    def agregar_vagon(self, vagon):
        self.vagones.append(vagon)

    def subir_pasajero(self, pasajero):
        for vagon in self.vagones:
         if len(vagon.sillas) < 10:  # Asumiendo que cada vagón tiene 10 sillas
            vagon.ocupar_silla(pasajero.boleto.numero_silla, pasajero)
            self.personas_subidas += 1
            return
    print("No hay sillas disponibles en ningún vagón.")


    def bajar_pasajero(self, numero_silla):
        for vagon in self.vagones:
            if numero_silla in vagon.sillas:
                vagon.liberar_silla(numero_silla)
                self.personas_bajadas += 1
                return
        print(f"No se encontró pasajero en la silla {numero_silla}.")

    def listar_pasajeros(self):
        pasajeros = []
        for vagon in self.vagones:
         pasajeros.extend(vagon.obtener_pasajeros())
         return pasajeros

    def contar_pasajeros_por_genero(self):
        conteo = {"M": 0, "F": 0}
        for pasajero in self.listar_pasajeros():
            if pasajero.genero in conteo:
                conteo[pasajero.genero] += 1
        return conteo

    def ordenar_pasajeros_por_edad(self):
        return sorted(self.listar_pasajeros(), key=lambda p: p.edad)

    def calcular_total_pagado(self):
        total = 0
        for pasajero in self.listar_pasajeros():
          total += pasajero.get_boleto().precio
        return total


    def mostrar_estadisticas(self):
        print(f"Personas subidas: {self.personas_subidas}")
        print(f"Personas bajadas: {self.personas_bajadas}")
        print(f"Total pagado: {self.calcular_total_pagado()}")

    def buscar_pasajero(self, nombre):
        for pasajero in self.listar_pasajeros():
            if pasajero.nombre == nombre:
                return pasajero
        return None