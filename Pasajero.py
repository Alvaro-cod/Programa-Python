class Pasajero:
    def __init__(self, nombre, edad, genero, boleto):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self.boleto = boleto

     # da el nombre del pasajero.
    @property
    def nombre(self):
        return self._nombre

    # nos proporciona su edad
    @property
    def edad(self):
        return self._edad

    # nos proporciona su genero
    @property
    def genero(self):
        return self._genero

    def get_boleto(self):
        return self.boleto

    # da el valor del boleto del pasajero.
    def set_boleto(self, boleto):
        self.boleto = boleto

