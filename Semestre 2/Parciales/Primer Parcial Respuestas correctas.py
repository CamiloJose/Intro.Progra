"""

    Instituto Tecnologico De Costa Rica

    Primer parcial

    Segundo Semestre

    Profesor: Jeff Schmidt Peralta

    Respuestas Correctas Del Parcial

"""

#   Ejercicio 1

def par2(num):
    if isinstance(num,int):
        return par2_aux(num,0)
    else: return "No hay 2 Pares"

def par2_aux(num,exponente):
    if num == 0:
        return 0
    elif (num%10)%2 ==0:
        return num%10*10**exponente + par2_aux(num//10, exponente + 1)
    else: return par2_aux(num//10, exponente)
# Eencontro todos los pares, no solo los 2 mas significativos

#   Ejercicio 2
def diferencia(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        return diferencia1(num1,num2,[],num2)+diferencia1(num2,num1,[],num1)#quitar repetidos
    else:
        return "error"

def diferencia1(num1,num2,lista,num2tmp):
    if num1==0:
        return lista
    elif num1%10==num2%10:
        return diferencia1(num1//10,num2tmp,lista,num2tmp)
    elif num2==0:
        lista.append(num1%10)
        return diferencia1(num1//10,num2tmp,lista,num2tmp)
    else:
        return diferencia1(num1,num2//10,lista,num2tmp)

#   Ejercicio 3
def moda(lista):
    if isinstance(lista,list):
        return verificar_contar(lista,lista,-1)
    else:
        return "error"

def contar(num,lista,repeticiones,pos):
    if pos==len(lista):
        return(num,repeticiones)
    
    elif num==lista[pos]:
        return contar(num,lista,repeticiones+1,pos+1)
    else:
        return contar(num,lista,repeticiones,pos+1)

def verificar_contar(lista,listatmp,num):
    if len(lista)==2:
        return num
    elif contar(lista[0],listatmp,-1,0)[1]>contar(lista[1],listatmp,-1,0)[1]:
        return verificar_contar(lista[1:],listatmp,lista[0])
    elif contar(lista[0],listatmp,-1,0)[1]<contar(lista[1],listatmp,-1,0)[1]:
        return verificar_contar(lista[1:],listatmp,lista[1])
    else:
        return verificar_contar(lista[1:],listatmp,-1)

#   Ejercicio 4
def intercambiar(num):
    if isinstance(num,int):
        return intercambiar_aux(0,num,0)
    else:
        return "error"
    
def intercambiar_aux(nuevo,num,exp):
    if num==0:
        return nuevo
    else:
        nuevo=nuevo+((num%10)*10**(exp+1))+((num%100//10)*10**(exp))
        return intercambiar_aux(nuevo,num//100,exp+2)


        
        
    
    
    
        


    

    

    

    
