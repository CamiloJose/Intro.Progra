#Sacar los divisores  de un numero entero

def divis(num):
    if isinstance(num, int):
        return divisores_aux(num,2)
    else:
        return "Error esta mal"

def divisores_aux(num, div):
    if num == div:
        return []
    elif num%div == 0:
        return [div] + divisores_aux(num, div +1)
    else: return divisores_aux(num, div +1)
# Proff

def divisores(numero):
    if isisnstance(numero, int):
        if numero == 0 or numero ==1:
            return[]
        else:
            return divisores_aux(numero, 2)
    else: return "Error: el valor ingresado no es numero"

def divisores_aux(numero, contador):
    if contador == numero: #Rojo
        return []
    elif numero % contador == 0: #erde
        return [contador[ + divisores_aux(numero, contador + 1)
    else: return divisores_aux(numero, contador + 1)
