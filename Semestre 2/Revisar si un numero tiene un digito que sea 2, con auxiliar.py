#Ejemplo de recursividad SIMPLE

#E:numero
#S:booleano que indique si tiene un 2
#R:Tiene que ser un numero entero

def tiene2(num):    #Funcion principal
    if isinstance(num,int):
        return tiene2_aux(abs(num))
    else:
        return "Error"

def tiene2_aux(num):
    if num ==0: #caso base 1
        return False
    elif num%10 ==2:
        return True
    else:
        return tiene2_aux(num//10)
