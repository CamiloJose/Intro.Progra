
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def getLado(self):
        return self.lado
    def setLado(self,nuevo):
        self.lado = nuevo
    def calculeArea(self):
        return self.lado ** 2
    def calculePerimetro(self):
        return self.lado * 4
