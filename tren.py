class Tren:
    def __init__(self, paradas):
        self.vagones = []
        self.paradas = paradas
        self.personas_subidas = 0
        self.personas_bajadas = 0

    # esto agrega un vagón a la lista de vagones del tren.
    def agregar_vagon(self, vagon):
        self.vagones.append(vagon)

     # esta funcion permite subir los pasajeros al tren.
    def subir_pasajero(self, pasajero):
        for vagon in self.vagones:
         if len(vagon.sillas) < 10:  #cada vagón tiene 10 sillas
            vagon.ocupar_silla(pasajero.boleto.numero_silla, pasajero)
            self.personas_subidas += 1
            return
    print("No hay sillas disponibles en ningún vagón.")


    # esta funcion baja un pasajero con la silla que le ponemos en consola
    def bajar_pasajero(self, numero_silla):
        for vagon in self.vagones:
            if numero_silla in vagon.sillas:
                vagon.liberar_silla(numero_silla)
                self.personas_bajadas += 1
                return
        print(f"No se encontró pasajero en la silla {numero_silla}.")

    # da una lista con los pasajeros que hay en el tren.
    def listar_pasajeros(self):
        pasajeros = []
        for vagon in self.vagones:
         pasajeros.extend(vagon.obtener_pasajeros())
         return pasajeros

    # Cuenta el número de pasajeros que hay  por género (M o F).
    def contar_pasajeros_por_genero(self):
        conteo = {"M": 0, "F": 0}
        for pasajero in self.listar_pasajeros():
            if pasajero.genero in conteo:
                conteo[pasajero.genero] += 1
        return conteo

    # Ordena  los pasajeros por edad.
    def ordenar_pasajeros_por_edad(self):
        return sorted(self.listar_pasajeros(), key=lambda p: p.edad)

    #   Calcula el total pagado por todos los pasajeros que hayan.
    def calcular_total_pagado(self):
        total = 0
        for pasajero in self.listar_pasajeros():
          total += pasajero.get_boleto().precio
        return total

    # muestra cuantas personas hay subidas y lo que han pagado
    def mostrar_estadisticas(self):
        print(f"Personas subidas: {self.personas_subidas}")
        print(f"Personas bajadas: {self.personas_bajadas}")
        print(f"Total pagado: {self.calcular_total_pagado()}")

    # Busca un pasajero por su nombre y nos da la informacion de el.
    def buscar_pasajero(self, nombre):
        for pasajero in self.listar_pasajeros():
            if pasajero.nombre == nombre:
                return pasajero
        return None
