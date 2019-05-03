#Invertir una lista, sin crear una nueva lista
#lista tiene que ser par
#con clases
class invertir(object):
    def __init__(self):
        pass
    
    def invertir(self, lista):
        if isinstance(lista, list) and len(lista)%2 ==0:
            return self.invertir2_aux(lista, 0, len(lista)-1)
        else:
            return "ERROR la lista no es par"

##    def invertir_aux(self, lista, indice, final):
##        if indice - 1 == indice2:
##            return lista
##        else:
##            t = lista[0][-1]
##            lista[0][-1] = lista[-1][0]
##            lista[-1][0] = t
##            return transponerMatriz_aux(lista, indice + 1, indice2 - 1)

    def invertir2_aux(self, lista, principio, final):
        #Otra forma de parar
        #if principio > final:
        #   return lista
        if principio -1 == final:
            return lista
        else:    
            lista[principio], lista[final] = lista[final], lista[principio]
            return self.invertir2_aux(lista, principio + 1, final -1)

lista =[1,2,3,4,5,6,7,8,9,10,11,12]
i = invertir()
print (i.invertir(lista))
