#Crear un cuadro magico, que en una tabla cuadrada
#las sumas de cada columna, fila y diagonal sean iguales

#Crear una tabla que verifique si los numeros estan  conseutivos de el 1 a el n
#y responder con un true o false

class Buscar(object):
    def __int__(self):
        pass
    def busqueda(self, num, lista):
        if isinstance(num, int) and isinstance(lista, list):
            return self.busqueda_aux(num, lista, 0)
        else: return "Error"

    def busqueda_aux(self, num, lista, indice):
        if lista == []:
            return -1
        elif lista[0] == num:
            return indice
        else: return self.busqueda_aux(num,lista[1:],indice + 1)

##num = 6
##lista = [6,8,3,9,5]
##b = Buscar ()
##b.busqueda(num, lista)
##print(b.busqueda(num, lista))


class Consecutivos(object):
    def __init__(self):
        pass

    def verificar(self, matriz, num):
        if isinstance(matriz, list) and isinstance(num,int):
            return self.buscar_aux(matriz)
        else: return "La matriz no es una lista"

    def buscar_aux(self, num, matriz, fila, columna):
        if len(matriz)==fila:
            return False
        elif columna == len(matriz[0]):
            return self.buscar_aux(num, matriz, fila+1, columna)
        elif matriz[fila][columa] == num:
            return True
        else: return self.buscar_aux(num, matriz, fila, columna+ 1)
        
##    def buscar2_aux()



#Proff

#Si fucniona
        
class Consecutivos(object):
    def __int__(self):
        pass
    def conse(self, matriz):
        if isinstance(matriz, list) and len(matriz) == len(matriz[0]):
            return self.conse_aux(matriz, 1)
        else: return "AAAHHHHHHH"

    def conse_aux(self, matriz, contador):
        if contador > (len(matriz)*len(matriz[0])):
            return True
        elif (self.buscar(contador, matriz, 0, 0)):
            return self.conse_aux(matriz, contador + 1)
        else: return False

    def buscar(self, elemento, matriz, fila, columna):
        if fila == len(matriz):
            return False
        elif columna == len(matriz[0]):
            return self.buscar(elemento, matriz, fila + 1, 0)
        elif elemento == matriz[fila][columna]:
            return True
        else: return self.buscar(elemento, matriz, fila, columna + 1)

c = Consecutivos()
matriz = [[3,2,7],[1,4,8],[5,6,9]]
print(c.conse(matriz))
