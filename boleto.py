class Boleto:
    def __init__(self, numero_vagon, numero_silla, tipo, edad):
        self._numero_vagon = numero_vagon
        self._numero_silla = numero_silla
        self._tipo, self._valor_boleto = self._calcular_precio(edad)

    def _calcular_precio(self, edad):
        if edad <= 12:
            return 'A', 2000  # Infante
        elif 13 <= edad <= 24:
            return 'B', 4000  # Adolescente
        elif  edad >= 25:
            return 'C', 6000  # Adulto mayor
        else:
            return 'N/A', 0  # No aplica

    @property
    def precio(self):
        return self._valor_boleto

    def get_numero_asiento(self):
        return f"{self._numero_vagon}-{str(self._numero_silla).zfill(2)}"

    @property
    def numero_vagon(self):
        return self._numero_vagon

    @property
    def numero_silla(self):
        return self._numero_silla

    @property
    def tipo(self):
        return self._tipo
