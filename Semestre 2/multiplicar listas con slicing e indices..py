

def multi(lista):   #Versión  con slicing
    if isinstance(lista,list) and lista != []:
        return multi_aux(lista,1)
    else: return"Error"

def multi_aux(lista,mult):
    if lista == []:
        return mult
    else: return multi_aux(lista[1:], mult*lista[0])

def multi2(lista):  #Versión  con índices
    if isinstance(lista,list) and lista !=[]:
        return multi2_aux(lista,0,len(lista),1)
    else: return "Error"

def multi2_aux(lista,i,n,mult):
    if i ==n:   #caso base
        return mult
    else: return multi2_aux(lista,i+1,n,mult*lista[i])
