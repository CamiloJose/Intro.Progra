#Encontrar un numero uy devolver su posicion

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

"""
num = 5
lista = [6,8,3,9,5]
b = Buscar ()
b.busqueda(num, lista)
print(b.busqueda(num, lista))
"""

#Lo mismo pero encontrar en numero sin importar la posicion

class Buscar(object):
    def __int__(self):
        pass
    def busqueda_1(self, num, lista):
        if isinstance(num, int) and isinstance(lista, list):
            return self.busqueda_1_aux(num, lista, 0, [])
        else: return "Error"

    def busqueda_1_aux(self, num, lista, indice, concatena):
        if len(lista) == indice:
            return concatena
        elif lista[indice] == num:
            return self.busqueda_1_aux(num,lista, indice + 1, concatena + [indice])
        else: return self.busqueda_1_aux(num,lista, indice + 1, concatena)


num = 3
lista = [6,8,3,9,5,3,5,4,3,1,4]
b = Buscar ()
b.busqueda_1(num, lista)
#nos dio por hacerlo bonito
print("   " * 8)
print("Se busco el numero",": ", num)
print("---" * 8)
print(b.busqueda_1(num, lista))
