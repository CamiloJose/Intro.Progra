#===================================================================================================================

#Crear una matriz de n x n en clases
class Matriz():
    def __init__(self):
        pass
    
    def crearMatriz(self,n):
        if isinstance(n, int) and n > 0:
            return self.crearMatriz_aux(n, [], [], 0, 0)

        else: return "AAHHHHHH"

    def crearMatriz_aux(self, n, matriz, fila, indiceFila, indiceColumna):
        if indiceFila == n:
            return matriz
        elif indiceColumna == n:
            return (self.crearMatriz_aux(n, matriz + [fila], [], indiceFila + 1, 0))
        elif indiceFila == 0 or indiceFila == (n-1):
            return (self.crearMatriz_aux(n, matriz, fila + ["*"], indiceFila, indiceColumna + 1))
        elif indiceColumna == 0 or indiceColumna == (n-1):
            return (self.crearMatriz_aux(n, matriz, fila + ["*"], indiceFila, indiceColumna + 1))
        else: return (self.crearMatriz_aux(n, matriz, fila + [0], indiceFila, indiceColumna + 1))

m = Matriz()
print("="*115)
print(m.crearMatriz(5))
print(" "*115)
print("="*115)

#========================================================================================

#Crear una matriz de n x m en clases
class Matriz2():
    def __init__(self):
        pass
    
    def crearMatriz(self,n, m):
        if isinstance(n, int) and n > 0:
            return self.crearMatriz_aux(n, m, [], [], 0, 0)

        else: return "AAHHHHHH"

    def crearMatriz_aux(self, n, m, matriz, fila, indiceFila, indiceColumna):
        if indiceFila == n:
            return matriz
        elif indiceColumna == m:
            return (self.crearMatriz_aux(n, m, matriz + [fila], [], indiceFila + 1, 0))
        elif indiceFila == 0 or indiceFila == (n-1):
            return (self.crearMatriz_aux(n, m, matriz, fila + ["*"], indiceFila, indiceColumna + 1))
        elif indiceColumna == 0 or indiceColumna == (n-1):
            return (self.crearMatriz_aux(n, m, matriz, fila + ["*"], indiceFila, indiceColumna + 1))
        else: return (self.crearMatriz_aux(n, m, matriz, fila + [0], indiceFila, indiceColumna + 1))

m1 = Matriz2()
print(" "*115)
print(m1.crearMatriz(5, 6))
print(" "*115)
print(">" *115)
