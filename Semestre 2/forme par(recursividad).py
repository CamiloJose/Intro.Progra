def forme_par(num):
    if isinstance(num,int):
        return forme_par_aux(abs(num))
    else:
        return"Error"

def forme_par_aux(num):
    exponente=0
    if num ==0:
        return 0
    elif num %2 ==0:
        return forme_par_aux(num**exponente+(num//10))
    else:
        return forme_par_aux(num//10)
