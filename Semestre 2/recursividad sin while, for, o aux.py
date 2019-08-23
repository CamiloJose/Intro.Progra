# Suma los digitos de un numero

    #Vercion 1
def suma(num):
    if isinstance(num, int):
        if num ==0:
            return 0
        else:
            return num % 10+ suma(num//10)
    else:
        return "Error"

    #Vercion 2
def suma2(num):
    if isinstance(num,int):
        return suma_aux(num)
    else:
        return "Error"
    
def suma_aux(num):
    if num ==0:
            return 0
    else:
        return num % 10+ suma(num//10)
