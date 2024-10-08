class Boleto:
    def __init__(self, numero_vagon, numero_silla, tipo, edad):
        self._numero_vagon = numero_vagon
        self._numero_silla = numero_silla
        self._tipo, self._valor_boleto = self._calcular_precio(edad)

      # Calcula el precio del boleto dependiendo de la edad del pasajero.
    def _calcular_precio(self, edad):
        if edad <= 12:
            return 'A', 2000  # Infante
        elif 13 <= edad <= 24:
            return 'B', 4000  # Adolescente
        elif  edad >= 25:
            return 'C', 6000  # Adulto mayor
        else:
            return 'N/A', 0  # No aplica

      # da el precio del boleto.
    @property
    def precio(self):
        return self._valor_boleto

    def get_numero_asiento(self):
        return f"{self._numero_vagon}-{str(self._numero_silla).zfill(2)}"

      # nos permite ver  el número del vagón.
    @property
    def numero_vagon(self):
        return self._numero_vagon

    # nos permite ver el numero de la silla
    @property
    def numero_silla(self):
        return self._numero_silla

    @property
    def tipo(self):
        return self._tipo
