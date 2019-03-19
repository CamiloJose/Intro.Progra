#Listas.
#Recurcion de cola__con classes__
class Operaciones:
    def __ini__(self):
        pass
    def largo(self, num):
        if isinstance(num, int):
            return self.largo_aux(num, 0)
        else:
            return "Error: el numero no s entero"
    def largo_aux(self, num, resultado):
        print (resultado, end=" -- ")
        if (num == 0):
            return resultado
        else:
            return self.largo_aux(num // 10, resultado + 1)
