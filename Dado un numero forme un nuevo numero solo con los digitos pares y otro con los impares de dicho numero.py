#Dado un numero forme un nuevo numero solo con los digitos pares de dicho numero
# y otro con los impares.
#Utilize While

class NuevoNumero:
    def __init__(self):
        pass

    #Proff
    def forme_listas(self,num):
        if isinstance(num, int):
            return self.forme_listas_aux(num,0,0,0,0)
        else:return "No es lista"

    def forme_listas_aux(self,num, contador, contador2, resultado, resultado2):
        while num >0:
            digi = num%10
            if digi%2 ==0:
                resultado += (digi*10**contador2)
                contador2 +=1
                num//=10
            else:
                resultado2 += digi*10**contador2
                contador2 += 1
                num = num//10

        print("Par", resultado)
        print("Impar", resultado2)

NN = NuevoNumero()
print(NN.forme_listas(14538))

#Por los dos contadores sale el numero grande
