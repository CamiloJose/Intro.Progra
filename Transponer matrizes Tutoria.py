
#=================================================================================


def transponer_Matriz(matriz):
    if (isinstance(matriz, list) and matriz!=[]):
        return transponerMatriz_aux(matriz, 0, 0)
    else: return "La matriz no es una lista."
#sumar
def transponerMatriz_aux(matriz, fila, columna):
    if fila == len(matriz):
        return matriz
    elif columna == len(matriz[0]):
        return transponerMatriz_aux(matriz, fila + 1, 0)
    else:
        if columna > fila:
            t = matriz[columna][fila]
            matriz[columna][fila] = matriz[fila][columna]
            matriz[fila][columna] = t
        return transponerMatriz_aux(matriz, fila, columna+ 1 )




def trans(matriz,result):
    if (isinstance(matriz, list) and matriz!=[]):
        return trans_copy(matriz,0,0,result)
    else:
        return "not list"

def trans_copy(matriz,i,j,result):
    if (i == len(matriz)):        
        return result
    elif (j == len(matriz[0])):
        return trans_copy(matriz,i+1,0,result)
    else:
        result[j][i] = matriz[i][j]
        return trans_copy(matriz,i,j+1,result)



## creacion de una matriz
#-------------
def creatematriz(i,j):
    return getmatriz(i,0,j,0, [],[])

def getmatriz(i,contadori,j,contadorj, fila,matriz):
    if contadori == i:
        return matriz
    elif contadorj == j:
        matriz.append(fila)
        return getmatriz(i,contadori+1,j,0, [],matriz)
    else:
        fila.append(0)
        return getmatriz(i,contadori,j,contadorj+1, fila,matriz)
    
#-------------
def create_inv(matriz):
    filas = len(matriz)
    cols  = len(matriz[0])
    return creatematriz(cols,filas)

matriz = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
result = create_inv(matriz)


print(" ",matriz,"\n",trans(matriz, result))

#________________________________




