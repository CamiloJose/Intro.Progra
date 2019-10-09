#Ejercicio 1
def sueldos(lista):
    if isinstance(lista,list):
        return sueldos_rec_aux(lista,0,0,0,0,0,len(lista),1)
    else: return "Error"

def sueldos_rec_aux(lista,mayor,menor,alto,promedio,i,n,flag):
    if flag == 0:   #caso base
        return [mayor,menor,alto_func(lista,0,len(lista),0),int(promedio)]
    else:
        if i<n:
            if lista[i] >= 1000000:
                return sueldos_rec_aux(lista,mayor+1,menor,alto,promedio + lista[i], i+1, n, flag)
            elif lista[i] < 1000000:
                return sueldos_rec_aux(lista,mayor,menor+1,alto,promedio + lista[i], i+1, n, flag)
            elif lista[i] > lista[i+1] and i<n-1:
                alto == lista[i]
                return salarios_rec_aux(lista,mayor,menor,lista[i],promedio, i+1,n,flag)
            elif lista[i] < lista[i]:
                alto == lista[i+1]
                return sueldos_rec_aux(lista,mayor,menor,alto,promedio,i,n,flag)
                
        elif i ==n:
            return sueldos_rec_aux(lista,mayor,menor,alto,promedio/n,i,n,0)
        elif i ==n-1:
            return sueldos_rec_aux(lista,mayor,menor,alto,promedio,i,n,0)

def alto_func(lista,i2,n2,result):
    if i2 == n2-1:
        return result
    else:
        if lista[i2] > lista[i2+1]:
            return alto_func(lista,i2+1,n2,result)
        else:
            result = lista[i2+1]
            return alto_func(lista,i2+1,n2,result)

#Ejercicio 2

def mas_par(lista):
    if isinstance(lista,list):
        return mas_par_aux(lista,0,0)
    else: return "Error"

def mas_par_aux(lista,par,impar):
    if lista ==[]: #caso base 1
        return False
    elif lista[0]%2 ==0:
        return mas_par_aux(lista,par+1,impar)
    else:
        return mas_par_aux(lista,par,impar)
