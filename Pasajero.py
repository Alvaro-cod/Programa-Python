class Pasajero:
    def __init__(self, nombre, edad, genero, boleto):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self.boleto = boleto

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def genero(self):
        return self._genero

    def get_boleto(self):
        return self.boleto

    def set_boleto(self, boleto):
        self.boleto = boleto

