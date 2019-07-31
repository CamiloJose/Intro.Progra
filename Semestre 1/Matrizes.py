# Matrizes
#Suma de matrizes

def suma_matriz(matriz1, matriz2):
    if (isinstance(matriz1, list) and matriz1 !=[] and isinstance(matriz2, list) and matriz2 != []):
        return matriz_aux(matriz1, matriz2, 0, 0, [], [])
    else: return "La matriz no es una lista."

def matriz_aux (matriz1, matriz2, f, c, rMat, fila):
    if f == len (matriz1):
        return rMat
    elif c == len(matriz1[0]):
        return matriz_aux(matriz1, matriz2, f+1, 0, rMat + [fila], [])
    else: return (matriz_aux(matriz1, matriz2, f, c+1, rMat, fila + [matriz1[f] [c] + matriz2[f] [f]]))

#Ejercicio
#Dada una matriz n x n, sumar los valores de su diagonal.
#Utilice recurcion de cola e indices.
#Crear una clase y la funcion de validacion

class Matriz_Diagonal(object):
    def __init__(self):
        pass
    def matriz_D(self, matriz1):
        if (isinstance(matriz1, list) and matriz1 !=[]):
            return matriz_D_aux(matriz1, 0, 0, [], [])
        else: return "La matriz no es una lista."
        

    def matriz_D_aux(self, matriz1, resultado,colfila):#(self, matriz1, matriz2, f, c, rMat, fila):
        if colfila ==len(matriz1):
            return fila
         #c  == len(matriz1[0]):
        else: return matriz_D_aux(matriz1, resultado + matriz1[colfila][colfila],colfia + 1)


        
""" Proffe
    Respuesta
"""



def suma_diagonal(matriz):
    if isinstance(matriz1, list) and matriz1 !=[] and len(matriz) == len (matriz):
        return diagonal_aux(matriz, len(matriz), 0, 0)
    else:
        return "Error"

def diagonal_aux(matriz, largo, fila, suma):
    if fila == largo:
        return suma
    else: return diagonal_aux(matriz, largo, fila + 1, suma + matriz[fila][fila])





    
# Diagonal inversa
#ejercicio igual al anterior pero la diagonal esta inversa

class Matriz_Diagonal(object):
    def __init__(self):
        pass
    def matriz_D_inversa(self, matriz1):
        if (isinstance(matriz1, list) and matriz1 !=[]):
            return self.matriz_D_inversa_aux(matriz1, 0, len(matriz1)-1, 0)
        else: return "La matriz no es una lista."
        

    def matriz_D_inversa_aux(self, matriz1, resultado,fila, columna):
        if fila == -1:
            return resultado
        else: return self.matriz_D_inversa_aux(matriz1, resultado + matriz1[fila][fila],fila - 1, columna +1)
