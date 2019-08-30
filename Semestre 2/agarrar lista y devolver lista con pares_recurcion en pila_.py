#sin indices
def cuales_pares(lista):
    if isinstance(lista,list):
        return cuales_pares_aux(lista)
    else: return "Error"

def cuales_pares_aux(lista):
    if lista == [ ]:    #caso base
        return [ ]
    elif lista[0]%2 == 0:
        return [lista[0]] + cuales_pares_aux(lista[1:])
    else:
        return cuales_pares_aux(lista[1:])
#______________________________
#con incices
def cuales_pares2(lista):
    if isinstance(lista,list):
        return cuales_pares2_aux(lista, 0, len(lista))
    else: return "Error"

def cuales_pares2_aux(lista, i, n):
    if i == n:    #caso base
        return []
    elif lista[i]%2 == 0:
        return [lista[i]] + cuales_pares2_aux(lista, i + 1, n)
    else:
        return cuales_pares2_aux(lista, i+1, n)
