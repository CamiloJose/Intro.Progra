def multi(lista):   #ver1 con slicing
    if isinstance(lista,list) and lista != []:
        return multi_aux(lista)
    else: return "Error"

def multi_aux(lista):
    if lista == []:    # casso base
        return 1
    else:
        return lista[0]*multi_aux(lista[1:])

def multi2(lista):  #ver2 con indices
    if isinstance(lista,list) and lista != []:
        return multi2_aux(lista,0, len(lista))
    else:return "Error"

def multi2_aux(lista,i,n):
    if i == n:  #caso base
        return 1
    else:
        return lista[i]*multi2_aux(lista, i+1,n)

