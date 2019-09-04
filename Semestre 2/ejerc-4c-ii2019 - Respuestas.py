import sys
sys.setrecursionlimit(3000)
#Ejercico 1
    #E: numero
    #S: sumatoria de cocientes hasta ese numero
    #R: numero entero
def suma_coc(n):
    if isinstance(n, int):
        return suma_coc_aux(n,1)
    else:return "Error"
def suma_coc_aux(n, i):
    if i ==n:
        return 0
    else: 
        return i/(i*(i+1)) + suma_coc_aux(n,i+1)
#_____________________________________________________________
#Ejercico 2
    #E: numero
    #S: susecion numerica, junto con las llamadas recursivas realizadas
    #R: numero migual o mayor a 0
#x = 0
def  funcion(n):
    if isinstance(n, int) and n>=0:
        return funcion_aux(n)
    else: return "Error"

def funcion_aux(n):
    #global x
    print("f","(",n-1,") =", n-1)
    #x = x+1
    if n == 0:       #caso base 1
        return 0
    elif n == 1:    #caso base 2
        return 1
    else:
        return (2* funcion_aux(n-2)+(funcion_aux(n-1)))
#_____________________________________________________________
#Ejercico 3
    #E: numero
    #S: lus digitos invertidos
    #R: tiene que ser numero entero

def invertir(num):
    if isinstance(num,int):
        return invertir_aux(abs(num),3)
    else: return"Error"

def invertir_aux(num,exponente):
    if num ==0:
        return 0
    else:
        return num%10*(10**exponente)+invertir_aux(num//10,exponente-1)
   
#_____________________________________________________________
#Ejercico 4
    #E: numero entero
    #S: numero que tiene los numeros pares por cero
    #R: tiene que ser un numero entero

def cambia(num):
    if isinstance(num,int):
        return cambia_aux(abs(num),0)
    else:
        return"Error"

def cambia_aux(num,exponente):
    if num ==0: #caso base
        return 0
    elif num %2 ==0:    #ultimo digito par
        return cambia_aux(num//10,exponente+1)
    else:
        return  (num%10)*10**exponente + cambia_aux(num//10,exponente+1)
#_____________________________________________________________
#Ejercico 5
    #E: numero entero
    #S: lista de los numeros naturales menores en orden acendente
    #R: no pueden ser negativos

x1= []
def iota(num):
    if isinstance(num,int):
        return iota_aux(num)
    else: return"Error"

def iota_aux(num):
    if isinstance(num,list):
        if num == 0:
            return []
        else:
            return num-1, iota_aux(num)
        print(x1)
    else:
        return "Error"
#_____________________________________________________________
#Ejercico 7
    #E: lista
    #S: retorna booleano diciendo si hay numero par
    #R: tiene que ser lista
    
def hay_par(lista):
    condicion = lambda numero : numero % 2 == 0
    if isinstance(lista, list) and lista !=[]:
        return hay_par_aux(lista, condicion, [])
    else:
        return "Error"
def hay_par_aux(lista, condicion, resultado):
    if lista == []:
        return resultado
    elif condicion (lista[0]):
        return True
    else:
        return False
#_____________________________________________________________
#Ejercico 8
    #E: lista y elemento
    #S: retorna la lista y cambia el primer elemento por 0
    #R: tiene que ser lista
def cambiar(lista):
    condicion = lambda numero : numero % 2 == 0
    if isinstance(lista, list) and lista !=[]:
        return cambiar_aux(lista, condicion, [])
    else:
        return "Error"
def hay_par_aux(lista, condicion, resultado):
    if lista == []:
        return resultado
    elif numero % 2 == 0 (lista[0]):
        return True
    else:
        return False
