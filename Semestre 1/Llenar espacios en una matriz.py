#Llenar espacios en una matriz



def matriz_C(matriz):
    if isinstance(matriz, list):
        return llenar_aux(matriz, 0 , 0)
    else: return "No es matriz no se puede crear"

def llenar_aux(matriz, fila, columna):
    if columna == len(matriz[0]):
        return matriz
    elif fila == 0 or fila == (len(matriz)-1):
        return (llenar_aux(matriz, fila, columna +1))
    elif columna == 0 or columna == (len(matriz[0])-1):
        matriz[fila][columna] = "*"
        return (llenar_aux(matriz, fila + 1, columna))

matriz_1 = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],]

rellemar= matriz_C(matriz_1)

print(rellemar)

#========================================================

#Proff

# ESTA SIRVE

class Matriz:
    def __init__(self):
        pass
    def rellenar(self, matriz):
        if isinstance(matriz, list):
            return self.rellenar_aux(matriz, 0, 0)
        else: "Error"

    def rellenar_aux(self, matriz, fila, columna):
        if fila == len(matriz):
            return matriz
        elif columna == (len(matriz[0])):
            return (self.rellenar_aux(matriz, fila+1, 0))
        elif fila == 0 or fila == (len(matriz)-1) or columna == 0 or columna == (len(matriz[0])-1):
            matriz[fila][columna] = "X"
            return (self.rellenar_aux(matriz, fila, columna + 1))
        else: return (self.rellenar_aux(matriz, fila, columna + 1))

m = Matriz()
matriz_2 = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
print("="*7)
print(m.rellenar(matriz_2))
