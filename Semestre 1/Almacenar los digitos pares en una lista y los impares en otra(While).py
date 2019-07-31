class Par_e_Impar:
    def __init__(self):
        pass
    
    def pares(self, num):
        if isinstance(num, int)and num >=0:
            return self.calculo(num)
        else:
            return "No es lista"


    def calculo(self, num):
        listasPares=[]
        listasImpares=[]
        while num>0:
            digi = num%10
            if (digi%2 == 0):
                listasPares += [digi]
            else: listasImpares += [digi]
            num = num//10
        return listasPares,listasImpares

su = Par_e_Impar()
print(su.pares(234567))
