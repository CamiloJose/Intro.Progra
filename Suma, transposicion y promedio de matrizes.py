#Transponer una matriz

#=======================================
    
def matriz_T(matriz):
    if (isinstance(matriz, list) and matriz!=[]):
        return get_col(matriz,0,0, 0, [])
    else: return "La matriz no es una lista."

def get_col(matriz, fila, columna, x, rcolumna):
    if fila == len(matriz):
        return matriz
    elif columna == len(matriz[0]):
        return (get_col(matriz, fila + 1, 0, x, rcolumna))
    else:
        if x == columna:
            rcolumna = rcolumna + [matriz[fila][columna]]
        return (get_col(matriz, fila, columna + 1, x, rcolumna))
    
#==================================================

class Suma_Matria(object):
    def __init__(self):
        pass
    def matriz_S(self,matriz):
        if (isinstance(matriz, list) and matriz!=[]):
            return self.promedio_aux(matriz, 0, 0, 0)
        else: return "La matriz no es una lista."

        #Sumar una matriz
    def suma_aux(self,matriz, fila, columna, resultado):
        if fila == len(matriz):
            return resultado
        elif columna == len(matriz[0]):
            return self.suma_aux(matriz, fila + 1, 0, resultado)
        else: return self.suma_aux(matriz, fila, columna+ 1, resultado + matriz[fila][columna])

        #Promedio de una matriz
class Promedio(object):
    def __init__(self):
        pass
        
    def matriz_P(matriz):
        if (isinstance(matriz, list)):
            return promedio_aux(matriz, 0, 0, 0)/(len(matriz)*len(matriz[0]))
        else: return "La matriz no es una lista."


    def promedio_aux(self, matriz, fila, columna, resultado):
        if fila == len(matriz):
            return resultado
        elif columna == len(matriz[0]):
            return promedio_aux(matriz, fila + 1, 0, resultado)
        else: return promedio_aux(matriz, fila, columna+ 1, resultado + matriz[fila][columna])


    matriz= [[1,2,3],
             [4,5,6],
             [7,8,9]]
    
    #promedio = self.matriz_P(matriz)
    #print(promedio)
