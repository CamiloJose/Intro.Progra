#Ejercicio 1
    #E:numero entero
    #S:digito mayor en un numero
    #R:numero entero

#cola
def mayor(num):
    if isinstance(num,int):
        return mayor_aux(abs(num), 0)
    else:
        return "Error"

def mayor_aux(num, i):
    if num ==0:
        return i
    elif num %10 > i:
        return mayor_aux(num//10, (i*0)+num%10)
    else: return mayor_aux(num//10,i)
    
#pila
def mayor2(num):
    if isinstance(num,int):
        return mayor2_aux(abs(num),0)
    else: return "Error"

def mayor2_aux(num,i):
    if num ==0:
        return i
    elif num %10 >= i:
        return (i*0)+num%10
    else: return mayor2_aux(num//10,i)
#_______________________________________________________________
#Ejercicio 2
    #E: numero y digito
    #S: los digitos del numero restados por el digito dado
    #R:numero entero

def restrard(dig, num):
    if isinstance(dig,int) and isinstance(num,int) and 0< dig < 10:
        return restrard_aux(dig, num, 0, 0)
    else: return "Error"

def restrard_aux(dig,num,i,r):
    if num ==0:
        return r
    elif (num%10) - dig<0:
        return restrard_aux(dig,num//10,i+1,r)
    else: return restrard_aux(dig,num//10,i+1,r+((num%10-dig)*10**i))
    
#_______________________________________________________________
    
#Ejercicio 3
    #E:numero
    #S:el numero con los digitos multiplos de 4 cambiados por 0
    #R:numero entero
def cambia(num):
    if isinstance(num, int):
        return cambia_aux(num,0,0)
    else: return "Error"

def cambia_aux(num, rest, exp):
    if num == 0:
        return rest
    elif (num%10)%4 ==0:
        return cambia_aux(num//10,rest, exp+1)
    else: return cambia_aux(num//10, rest +((num%10)*10**exp), exp+1)

#_______________________________________________________________
    
#Ejercicio 4
    #E:numero y digito
    #S: booleano si el numero tiene almenos UN  digito divisble por el digito dado
    #R:numero entero

def hay_div(num, dig):
    if isinstance(num,int) and isinstance(dig,int) and 0<dig<10:
        return hay_div_aux(num,dig)
    else: return "Error"

def hay_div_aux(num,dig):
    if num ==0:
        return False
    elif (num%10)%dig ==0:
          return True
    else: return hay_div_aux(num//10,dig)

#_______________________________________________________________
    
#Ejercicio 5
    #E:numero y digito
    #S: booleano si el numero tiene todos los digitos divisble por el digito dado
    #R: numero entero

def todos_div(num,dig):
    if isinstance(num,int) and isinstance(dig,int) and 0<dig<10:
        return todos_div_aux(num,dig,largo(num,0),0)
    else: return "Error"

def largo (num, i):
    if num ==0:
        return i
    else:
        return largo (num//10,i+1)

def todos_div_aux(num,dig,p,r):
    if r==p:
        return True
    elif (num%10)%dig ==0:
        return todos_div_aux(num//10,dig,p,r+1)
    else:return False
#_______________________________________________________________
    
#Ejercicio 6
    #E:numero
    #S: tupla cantidad con nueros pares e impares
    #R: numero entero

def revise_num(num):
    if isinstance(num,int):
        return revise_num_aux(num,0,0)
    else: return"Error"

def revise_num_aux(num,par,impar):
    if num ==0:
        return (par,impar)
    else:
        if (num%10)%2==0:
            return revise_num_aux(num//10,par+1,impar)
        else:
            return revise_num_aux(num//10,par,impar+1)
#_______________________________________________________________
    
#Ejercicio 7
    #E: digito y numero
    #S: tupla con numeros mayores o iguales al digito y la otra con los menores al digito
    #R: numero entero

def divida(dig,num):
    if isinstance(num,int):
        return divida_aux(num,dig, 0, 0,0,0)
    else:return"Error"

def divida_aux(num,dig,mayor,menor,exponenteM,exponentem):
    if num ==0:
        return (mayor,menor)
    else:
        if num %10 >=dig:
            return divida_aux(num//10,dig, mayor + num%10*10**exponenteM, menor, exponenteM+1,exponentem)
        else:
            return divida_aux(num//10,dig,mayor,menor + num %10*10**exponentem,exponenteM,exponentem+1)
#_______________________________________________________________
    
#Ejercicio 8
    #E: 2 numeros
    #S: numero con los digitos del primero que esten en el segundo
    #R: numero entero

def intersec(num1, num2):
    if isinstance(num1, int) and isinstance(num2,int):
        return intersec_aux(num1,num2,0,1)
    else:return "Error"

def intersec_aux(num1, num2,resultado,exponente):
    if num1==0 and num2==0:
        return resultado
    elif num1%10==num2%10:
        resultado = ((num1%10)*10**exponente)
        return intersec_aux(num1//10,num2//10,((num1%10*10**exponente)+(resultado*0) + (num2%10 + resultado*0)), exponente + 1)
    else:
        return intersec_aux(num1//10,num2//10,((num1%10*10**exponente)+(resultado*0) + (num2%10 + resultado*0)), exponente )
#_______________________________________________________________
    
#Ejercicio 9
    #E: serie de numeros
    #S: retorne el numero de la serie que se da
    #R: numero entero

def serie(num):
    if isinstance(num,int):
        return serie_aux(num,2,1)
    else: return "Error"

def serie_aux(num,inicial,contador):
    if (contador ==num):
        return inicial
    elif (contador%2 != 0):
        return serie_aux(num,inicial+3,contador +1)
    else: return serie_aux(num,inicial +2, contador +1)
#_______________________________________________________________
    
#Ejercicio 10
    #E: formula
    #S: limite superior de la sumatoria y el resultado hasta ese numero
    #R: numero entero

def sumatoria(n):
    if isinstance(n,int):
        return sumatoria_aux(n,1,1)
    else:
        return "Error"

def sumatoria_aux(n,i, contador):
    if n ==0:
        return i
    else: sumatoria_aux(n,i+(1/i),contador+1)
        
