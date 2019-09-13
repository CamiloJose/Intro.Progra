
def pares(lista):   #ver con slicing y append
    return pares_aux(lista,[])
def pares_aux(lista,lpares):
    if lista ==[]:
        return lpares
    elif lista[0]%2==0:
        lpares.append(lista[0])
        return pares_aux(lista[1:],lpares)
    else: return pares_aux(lista[1:],lpares)
        
