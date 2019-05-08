import math
from FiguraInicial import Fig

class Fig:
    def __init__(self, x, y):
        self.x = x
        self.__y = y

    def getX(self):
        return self.x
    
    def setX(self, x):
        if x >= 0 and x <= 1023:
            self.__x = x
        else: print("El valor de x debe ser mayor o igual a 0 y menor a 1024")
        
    def getY(self):
        return self.__y
    
    def setY(self, y):
        if y >= 0 and y <= 767:
            self.__y = y
        else: print("El valor de y debe ser mayor o igual a 0 y menor a 767")

class Circulo(Fig):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.__radio = r
    def getRadio(self):
        return self.__radio
    def getRadio(self):
        return self.__radio
    def setRadio(self, r):
        self.__radio = r
    def calcularArea(self):
        return math.pi * (self.__radio*2)