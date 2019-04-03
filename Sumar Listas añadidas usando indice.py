#Sumar listas anidadas con indices

#ESTE ES EL MIO
#NO Fucniona
class Lista(object):
    def __int__(self):
        pass
    def listas_aninadas(self, lista):
        if isinstance(lista, list):
            return self.anidadas_aux(lista, 0, 0)
        else:
            return "Error la cagaste"
            
    def anidadas_aux(self,lista, indice, resultado):
        if indice == len(lista):
            return resultado
        if isinstance(lista[indice], list):
            return self.anidadas_aux(lista[indice], 0, 0) + self.anidadas_aux(lista, indice + 1, resultado)
        else:
            return self.anidadas_aux(lista, indice+1, resultado + lista[indice])
#lista = [1,2[3,4,5,6],7,9]
"""
lista = [1,2,[3,4,5,8,],9,8]
l = listas_aninadas()
print(l.listas_aninadas(lista))
"""


#PROFFE
#Si SIRVE
class Recorridos(object):
    def __int__(self):
        pass
    def recorrerIndices(self, lista):
        if isinstance(lista, list):
            return self.recorrerIndices_aux(lista, 0, 0)
        else:
            return "Error la cagaste"
            
    def recorrerIndices_aux(self, lista, resultado, indice):
        if indice == len(lista):
            return resultado
        if isinstance(lista[indice], list):
            return (self.recorrerIndices_aux(lista[indice], 0, 0) + self.recorrerIndices_aux(lista, resultado, indice + 1))
        else:
            return self.recorrerIndices_aux(lista,resultado + lista[indice], indice + 1)


#Lista = [5, 8,19,[6,[8,9,10],11,12]
lista = [5, 8,19,[6,[7,8,],9, 10,],11,12]
ru = Recorridos()
print(ru.recorrerIndices(lista))
