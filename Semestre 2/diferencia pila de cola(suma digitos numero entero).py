    #E:numero
    #S:suma dígitos
    #R:numero entero
def suma(num):
    if isinstance(num,int): #Recursividad de pila
        return suma_aux(abs(num))
    else: return "Error"

def suma_aux(num):
    if num == 0: #caso base
        return 0
    else: return num%10 + suma_aux(num//10)

#RECURSIVIDAD DE COLA

def suma2(num):
    if isinstance(num,int):
        return suma_aux2(abs(num),0)
    else: return "Error"

def suma_aux2(num,result):
    if num ==0:
        return result
    else:
        return suma_aux2(num//10,result + num%10)
