#Ejercicio 1
    #E:numero
    #S:numeros con 1 digito
    #R:numero entero

def forme(num):
    if isinstance(num,int):
        return forme_aux(num,0)
    else: return "Error"

def forme_aux(num,exponente):
    if num ==0:
        return 0
    elif num % 10 ==1:
        return num%10*10**exponente+forme_aux(num//10,exponente + 1)
    else:
        return forme_aux(num//10, exponente)

#_______________________________________________________
#Ejercicio 2
    #E:numero
    #S:True of False
    #R:numero entero
def sumax(num1, num2):
    if isinstance(num1, int) and isinstance(num2,int):
        return sumax_aux(num1) >= sumax_aux(num2)
    else: return"Error"
def sumax_aux(num):
    if num ==0 :
        return 0
    else:
        return num%10 + sumax_aux(num//10)
#_______________________________________________________
#Ejercicio 3
    #E:dos numeros
    #S:multiplicacion de a y b
    #R:numero b tiene que ser entero
def multi(num1, num2):
    if isinstance(num2,int):
        return multi_aux(num1, num2-1)
    else: return "Error"

def multi_aux(num1, num2):
    if num2 ==0:
        return num1
    else: return num1 + (multi_aux(num1, num2-1))
#_______________________________________________________
#Ejercicio 4
    #E:numero
    #S:numeros pares sumados y numeros impares sumados
    #R:numero tiene que ser entero

def suma_parimpar(num):
    if isinstance(num,int):
        return suma_par(num), suma_impar(num)
    else: return"Error"

def suma_par(num):
    if num ==0:
        return 0
    elif num%2==0:
        return num%10+suma_par(num//10)
    else: return suma_par(num//10)

def suma_impar(num):
    if num ==0:
        return 0
    elif num%2==1:
        return num%10+suma_impar(num//10)
    else: return suma_impar(num//10)

#_______________________________________________________
#Ejercicio 5
    #E:numero entero
    #S:numero con cada digito menos 1
    #R:numero tiene que ser entero
def reste1(num):
    if isinstance(num,int):
        return reste1_aux(num,0)
    else: return "Error"

def reste1_aux(num, exponente):
    if num ==0:
        return 0
    else:
        if num%10 ==0:
            return (reste1_aux(num //10, exponente+1))
        else:
            return(num%10-1)*10**exponente+reste1_aux(num//10,exponente+1)
#_______________________________________________________
#Ejercicio 6
    #E:numeros
    #S:la formula dada
    #R:los numeros tienen que ser enteros y mayores a 0
def formula(a,n):
    if isinstance(a,int) and n >0:
        return formula_aux(a,n)
    else: return "Error"

def formula_aux(a,n):
    if n ==0:
        return 1
    else:
        return a**(n-1)+formula_aux(a,n-1)
