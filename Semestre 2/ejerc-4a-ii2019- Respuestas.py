#Ejercicio 1
    #E:numero
    #S:largo del numero
    #R:numero entero
def largo(num):
    if isinstance(num,int):
        return largo_aux(abs(num))
    else: return "Error"

def largo_aux(num):
    if num == 0:
        return 0
    else:
        return 1+largo_aux(num//10)
#___________________________________________________________
    #Ejercicio 2
    #E:numero entero
    #S:cantidad de veces que sale un numero
    #R:numero entre 0 y 9
def cuente_dig(num, n):
    if isinstance(num, int) and n>0:
        return cuente_dig_aux(num, n)
    else:return "Error"

def cuente_dig_aux(num, n):
    if num ==0:
        return 0
    elif num%10 ==n:
        return 1+cuente_dig_aux(num//10,n)
    else:
        return cuente_dig_aux(num//10,n)

#___________________________________________________________
    #Ejercicio 3
    #E:numero entero
    #S:numero par cantidad
    #R:numero entero

def cuente_par(num):
    if isinstance(num,int):
        return cuente_par_aux(num)
    else: return "Error"
    
def cuente_par_aux(num):
    if num ==0:
        return 0
    elif num%2 ==0:
        return 1+cuente_par_aux(num//10)
    else:
        return cuente_par_aux(num//10)

#___________________________________________________________
    #Ejercicio 4
    #E:numero entero
    #S:si el primer y el ultimo digito son iguales
    #R:numero entero

def iguales(num):
    if isinstance(num,int):
        return iguales_aux(num)
    else: return "Error"

def iguales_aux(num):
    ultimo = num%10
    if num ==0:
        return 0
    elif ultimo == ((num//10)+1):
        return True
    else: return False
