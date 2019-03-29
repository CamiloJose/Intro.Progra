#Crear una lista con los numeros pares(lambda)
#QUIZ 3 == Intro
def par(num):
    cond =lambda digito :digito%2 == 0
    if isinstance (num, int):
        return par_aux(num, cond)
    else: return par_aux(num, cond)

def par_aux(num,cond):
    if num == 0:
        return []
    elif cond(num%10):
        return [num%10]+par_aux(num//10,cond)
    else: return par_aux(num//10, cond)
