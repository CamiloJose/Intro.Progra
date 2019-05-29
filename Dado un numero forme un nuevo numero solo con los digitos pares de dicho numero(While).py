#Dado un numero forme un nuevo numero solo con los digitos pares de dicho numero.
#Utilize While
class NuevoNumero:
    def __init__(self):
        pass
# Funciona pero dio peresa quitarlo

##    def numero(self,num):
##        if isinstance(num, int)and num >=0:
##            return self.nuevo(num, 0, 0)
##        else:
##            return "No es lista"
##
##    def nuevo(self,num, contador, resultado):
##        while num >0:
##            if (num%10)%2 ==0:
##                resultado += (num%10)*10**contador
##                contador +=1
##                num =num//10
##
##            else: num = num//10
##        print(resultado)
    
    #Proff
    def forme_par(self,num):
        if isinstance(num, int)and num >=0:
            return self.forme_par_aux(num)
        else:return "No es lista"

    def forme_par_aux(self,num):
        result=0
        exp=0
        while num >0:
            digi = num%10
            if digi%2 ==0:
                result += (digi*10**exp)
                exp +=1
            num//=10
        return result

NN = NuevoNumero()
print(NN.forme_par(14538))
