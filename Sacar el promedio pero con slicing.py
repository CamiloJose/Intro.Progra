#matrizez sacar el promedio pero con slicing
def matriz_Slic(matriz):
        if (isinstance(matriz, list)):
            return promedio_slicing_aux(matriz, 0)/ (len(matriz)* len(matriz[0]))
        else: return "La matriz no es una lista, porqueeeeeeeeeeeeeeeeeeeeeeeeeeee????????????????."


def promedio_slicing_aux(matriz, resultado):
    if matriz == []:
        return resultado
    elif isinstance(matriz[0], list):
        return promedio_slicing_aux(matriz[0]+ matriz[1:], resultado)
    else: return promedio_slicing_aux(matriz[1:], resultado + matriz[0])
        

matriz= [[1,2,3],
         [4,5,6],
         [7,8,9]]

promedio = matriz_Slic(matriz)
print(promedio)
