#1
def digitos(num):
    if isinstance(num,int):
        return digitos_aux(num,0,0)
    else: return "error"
    
def digitos_aux(num, mayores, menores):
    while num != 0:
        if (num%10) <= 5:
            menores += 1
            num = num//10
        elif (num%10) > 5:
            mayores += 1
            num = num//10
    return (mayores, menores)

#2
def forma_par(num):
    if isinstance(num,int):
        return forma_par_aux(num,0,0)
    else: return "error" 

def forma_par_aux(num,par,indice):
    while num != 0:
        if (num%2)%2 == 0:
            par += ((num%10)*10**indice)
            indice += 1
            num =num//10
        else:
             num = num//10
    return par
         
#3
def todos_pares(num):
    if isinstance(num,int):
        return todos_pares_aux(num)
    else: return "error"

def todos_pares_aux(num):
    while num!=0:
        if (num%10)%2 == 0:
            num = num//10
        elif (num%10)%2 != 0:
            num = 0
            return False
    return True

#4

def factorial(num):
    if isinstance(num,int):
        return factorial_aux(num)
    else: return "error"
    
def factorial_aux(num):
    resultado = 1
    numero = 1
    while numero <= num:
        resultado *= numero
        numero += 1
    return resultado

#5
def fib(num):
    if isinstance(num,int):
        return fib_aux(num,0)
    else: return "error"

def fib_aux(num,i):
    actual = 1
    anterior = 0
    while i < num:
        siguiente = actual + anterior
        actual = anterior
        anterior = siguiente
        i = i + 1
    return siguiente
            
#6
def palindromo(num):
    if isinstance(num,int):
        return palindromo_aux(num)
    else: return "error"

def palindromo_aux(num):
    a = (largo_num(num,0)-1)
    while num != 0:
        if (num%10) == (num//(10**a)):
            num = num//10
            num = num//(10**a)
            a -= 1
        else: return False
    return True 
        

def largo_num(num,i):
    while num != 0:
        i += 1
        num = num//10
    return i

#7
def elimine(dig,num):
    if isinstance(dig,int) and isinstance(num,int):
        return elimine_aux(dig, num)
    else: return "Error"

def elimine_aux(dig, num):
    f = True
    exp = 0
    x = 0
    while f:
        if dig != num%10:
            x += num%10 * 10**exp
            exp += 1
            num//=10
        else:
            f = False
            num//=10
    x += num*10*exp
    return x
