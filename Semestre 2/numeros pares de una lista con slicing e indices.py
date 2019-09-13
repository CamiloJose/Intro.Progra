
def pares(lista):   #con slicing
    if isinstance(lista,list) and lista != []:
        return pares_aux(lista, [])
    else: return "Error"

def pares_aux(lista,lpares):
    if lista ==[]:
        return lpares
    elif lista[0]%2 ==0:
        return pares_aux(lista[1:],lpares + [lista[0]])
    else: return pares_aux(lista[1:], lpares)
