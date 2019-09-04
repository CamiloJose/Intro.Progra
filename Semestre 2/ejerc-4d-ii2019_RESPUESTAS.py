#Ejercicio 1
    #E: numero
    #S:tuplas
    #R:numero menor de dos digitos
def separa(num):
    if isinstance(num, int) and num >=10:
        return (separa_par_aux(num,0,0), separa_inpar_aux(num,0,0))
    else: return "Error"

def separa_par_aux(num,contador,exponente):
    if num ==0:
        return 0
    elif contador%2 ==0:
        return num%10*10**exponente + separa_par_aux(num//10, contador+1, exponente+1)
    else: return separa_par_aux(num//10,contador+1,exponente)

def separa_inpar_aux(num,contador2,exponente2):
    if num ==0:
        return 0
    elif contador2%2 !=0:
        return num%10*10**exponente2 + separa_inpar_aux(num//10, contador2+1, exponente2+1)
    else: return separa_inpar_aux(num//10,contador2+1,exponente2)
#__________________________________________________________________________
#Ejercicio 2
    #E: numero
    #S: deficiente, abundante o perfecto
    #R: numero menor de dos digitos
def clasifique(num):
    if isinstance(num,int):
        return clasificacion(num)
    else: return "Error"

def clasificacion(num):
    if clasifique_aux(num,num)>num:
        return "Abundante"
    elif clasifique_aux(num,num) == num:
        return "Perfecto"
    else:
        return"Deficiente"

def clasifique_aux(num,divisor):
    if divisor ==0:
        return 0
    else:
        if num == divisor:
            return  clasifique_aux(num,divisor-1)
        
        elif num%divisor ==0:
            return divisor + clasifique_aux(num,divisor-1)

        else:
            return clasifique_aux(num,divisor-1)
#__________________________________________________________________________
#Ejercicio 3
    #E: lista
    #S: promedio de la lista sin el dato mas pequeño y el mas grande
    #R: numeros enteros

def calificacion(lista):
    if isinstance(lista,list):
        return (calificacion_aux(lista, 0, len(lista)) - suma_max_min(lista)// len(lista)-2)
    else: return "Error"

def calificacion_aux(lista,i,n):
    if i == n:
        return 0
    else: return lista[i] + calificacion_aux(lista, i+1, n)

def suma_max_min(lista):
    return max(lista) + min(lista)

def calificacion_slicing(lista):
    if isinstance(lista,list):
        return (calificacion_slicing_aux(lista) - suma_max_min(lista)// len(lista)-2)
    else: return "Error"

def calificacion_slicing_aux(lista):
    if lista ==[]:
        return 0
    else: return lista[0] + calificacion_slicing_aux(lista[1:])
#__________________________________________________________________________
#Ejercicio 4
    #E: num
    #S: cantidad de digitos que aparecen en pares
    #R: numero entero

def parejas(num):
    if isinstance(num,int):
        return parejas_aux(num)
    else: return "Error"

def parejas_aux(num):
    if num == 0:
        return 0
    else:
        if num %10 == (num%100)//10:
            return 1 + parejas_aux(num//10)
        else: return parejas_aux(num//10)
#__________________________________________________________________________
#Ejercicio 5
    #E: lista y elemento
    #S: lista con el primer elemento removido
    #R: 
def eliminar(lista, ele):
    if isinstance(lista,list):
        return eliminar_aux(lista,ele,0, len(lista),1)
    else: return "Error"

#con indice
def eliminar_aux(lista,elemento,i,n,cont):
    if  i ==n:
        return []
    elif lista[i] == elemento and cont ==1:
        return [] + eliminar_aux(lista,elemento, i+1, n, cont -1)
    else: return [lista[i]] + eliminar_aux(lista,elemento, i+1, n, cont)

def eliminar_slicing(lista, ele):
    if isinstance(lista,list):
        return eliminar_slicing_aux(lista,ele,1)
    else: return "Error"

def eliminar_slicing_aux(lista,ele, cont):
    if lista ==[]:
        return []
    elif lista[0] == ele and cont ==1:
        return []+ eliminar_slicing_aux(lista[1:],ele,cont-1)
    else: return [lista[0]] + eliminar_slicing_aux(lista[1:],ele,cont)

#__________________________________________________________________________
#Ejercicio 6
    #E: lista y elemento
    #S: lista con todos los elemento removido
    #R: ---
def eliminar_todos(lista, ele):
    if isinstance(lista,list):
        return eliminar_todos_aux(lista,ele,0, len(lista))
    else: return "Error"

#con indice
def eliminar_todos_aux(lista,elemento,i,n):
    if  i ==n:
        return []
    elif lista[i] == elemento :
        return [] + eliminar_todos_aux(lista,elemento, i+1, n)
    else: return [lista[i]] + eliminar_todos_aux(lista,elemento, i+1, n)

def eliminar_todos_slicing(lista, ele):
    if isinstance(lista,list):
        return eliminar_todos_slicing_aux(lista,ele)
    else: return "Error"

def eliminar_todos_slicing_aux(lista,ele):
    if lista ==[]:
        return []
    elif lista[0] == ele:
        return []+ eliminar_todos_slicing_aux(lista[1:],ele)
    else: return [lista[0]] + eliminar_todos_slicing_aux(lista[1:],ele)

#__________________________________________________________________________
#Ejercicio 7
    #E: lista
    #S: lista con el primer elemento removido
    #R:

def frente2(lista):
    if isinstance(lista,list):
        return frente2_aux(lista)
    else: return "Error"
    

def frente2_aux(lista):
    if (len(lista) <= 2):
        return []
    else:
        return lista[:len(lista)-2]
    
#__________________________________________________________________________
#Ejercicio 8
    #E: lista
    #S: lista invertida
    #R: tiene que ser lista
def invierta(lista):
    if isinstance(lista,list):
        return invierta_aux(lista)
    else: return "Error"

def invierta_aux(lista):
    if lista == []:
        return []
    else:
        return lista[len(lista)-1:] + invierta_aux(lista[:len(lista) - 1])
"""
Funciona pero no lo vimos en clase:

    lista = ([0, 1, 2, 3, 4])

    invertida_lista = lista[::-1]

    invertida_lista

    >>>[4, 3, 2, 1, 0]
"""
