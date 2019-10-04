"""
Fecha: 14-8-2029
Semana: 4
Respuestas - ejerc-3b-ii2019.py
"""

#Ejercicio 1
    #E: Radio
    #S: Volumen, Area
    #R: radio mayor a 0
from math import pi
def esfera(radio):
    if radio > 0:
        Volumen = (4/3) * pi * (radio**3)
        Area = 4* pi * (radio**2)
        return Volumen, Area
#______________________________________________________
#Ejercicio 2
    #E: Numero, porcentaje
    #S: numero
    #R: no hay
def aumente(num, porcentaje):
    resultado= (num * porcentaje/100)+num
    return resultado
#______________________________________________________
#Ejercicio 3
    #E: Numero, digito
    #S: numero mas el digito al final del numero
    #R: el numero tiene que ser entero
def adjunto(num, dig):
    if isinstance(num, int):
        adjuncion = (num *10)+dig
        return adjuncion
    else: return "Error"
 #______________________________________________________
#Ejercicio 4
    #E: Numero entre 1 y 7
    #S: numero en forma romana
    #R: el numero tiene que estar entre 1 y 7
def romano(num):
    if isinstance(num, int) and num<=7 and num>=1:
        if num==1:
            return "I"
        if num==2:
            return "II"
        if num==3:
            return "III"
        if num==4:
            return "IV"
        if num==5:
            return "V"
        if num==6:
            return "VI"
        if num==7:
            return "VII"
    else: return "Error"
#______________________________________________________
#Ejercicio 5
    #E: metros, indicador
    #S: convercion en centimetros, pulgadas, pies, yardas
    #R: tiene que ser diferente de 0
def convertir(metros, indicador):
    if isinstance(metros, int) and indicador>=1 and indicador<=4:
        if indicador ==1:
            centimetros = metros * 100
            return centimetros
        if indicador ==2:
            pulgadas = (metros*100)/2.54
            return pulgadas
        if indicador ==3:
            pies = ((metros*100)/2.54)/12
            return pies
        if indicador ==4:
            yarda= (((metros*100)/2.54)/12)/3
            return yarda
#______________________________________________________
#Ejercicio 6
    #E: horas
    #S: salario y tarifa
    #R: tiene que ser diferente de 0
def calc_salario(horas):
    salario=10
    if isinstance(horas,int):
        if horas <= 40:
            salario1 = salario * horas
            return salario1
        if horas > 40:
            horas2 = horas-40
            salario2 = (horas2*((salario*0.5)+salario)) + salario*40
            tarifa = (horas2*((salario*0.5)+salario))
            return salario2, tarifa
    else: 'Error'
#______________________________________________________
#Ejercicio 7
    #E: numero
    #S: la tabla de multiplicar de este numero
    #R: tiene que ser diferente de 0
def tabla(num):
    if isinstance(num,int) and num>0:
        print("",num, "x 1 =",num*1, "\n",
              num, "x 2 =",num*2, "\n",
              num, "x 3 =",num*3, "\n",
              num, "x 4 =",num*4, "\n",
              num, "x 5 =",num*5, "\n")
#______________________________________________________
#Ejercicio 8
    #E: numero
    #S: nombre de el numero
    #R: tiene que estar entre 1 y 5
def num_letras(num):
    if isinstance(num, int) and num>=1 and num<=5:
        if num == 1:
            return"Uno"
        if num == 2:
            return"Dos"
        if num == 3:
            return"Tres"
        if num == 4:
            return"Cuatro"
        if num == 5:
            return"Cinco"
    else: return "Error"
        
#______________________________________________________
#Ejercicio 9
    #E: año
    #S: true o false
    #R: tiene que ser un año
def bisiesto(año):
    if (año%4 == 0 and año%100 != 0):
        return True
    else:
        return False
#______________________________________________________
#Ejercicio 10
    #E: 3 numeros
    #S: los 2 numeros en orden descendente
    #R: tienen que ser 3 numeros 
def orden (num1, num2, num3):
    if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
        if num1 < num2 and num1 < num3:
            return num3, num2, num1
        if num1 < num2 and num1>num3:
            return num2, num1, num3
        if num1> num2 and num1 > num3:
            return num1, num2, num3
        if num1>num3 and num2>num3:
            return num3, num2, num1
    else: "Error"
#______________________________________________________
#Ejercicio 11
    #E: numero de 3 digitos
    #S: los digitos invertidos
    #R: el numero no puede ser mayor o menor de 3 digitos
def invierta(num):
    if isinstance(num, int) and num>=100 and num <=999:
        if num>=100:
            dig1= num % 10
            op1= num //10
            dig2 = op1 % 10
            op2 = op1 //10
            dig3 = op2
            #return dig1, dig2, dig3
            return (dig1*100)+(dig2*10)+dig3
        
#______________________________________________________
#Ejercicio 12
    #E: numero de 4 digitos
    #S: si la suma de sus digitos es par
    #R: el numero no puede ser mayor  de 4 digitos o tener 4 ceros
def par(num):
    if isinstance(num, int) and num <=9999:
        #num de 2 digitos
        if num<100 and num>9:
            dig1= num % 10
            op1= num //10
            dig2 = op1

            result = dig1+dig2
            if result %2 ==0:
                return True
            else:
                return False
        #num de 3 digitos
        if num<1000 and num>99:
            dig1= num % 10
            op1= num //10
            dig2 = op1 % 10
            op2 = op1 //10
            dig3 = op2
            
            result = dig1+dig2+dig3
            if result %2 ==0:
                return True
            else:
                return False
        #Num de 4 digitos
        if num<10000 and num>999:
            dig1= num % 10
            op1= num //10
            dig2 = op1 % 10
            op2 = op1 //10
            dig3 = op2%10
            op3= op2//10
            dig4 = op3
            
            result = dig1+dig2+dig3+dig4
            if result %2 ==0:
                return True
            else:
                return False
        else: return "Error"
#______________________________________________________
#Ejercicio 13
    #E: numero de 3 digitos
    #S: diga si el 1 y el 3 digito son iguales o no
    #R: tiene que se un numero de 3 digitos
def iguales(num):
    if isinstance(num, int) and num <=999:
        if num<1000 and num>99:
            dig1= num % 10
            op1= num //10
            dig2 = op1 % 10
            op2 = op1 //10
            dig3 = op2

            if dig1==dig3:
                return True
            else:
                return False
#______________________________________________________
#Ejercicio 14
    #E: numero de 3 digitos
    #S: diga cual es el digito mas significativo
    #R: el numero tiene que ser de 3 digitos
def significativo(num):
    if isinstance(num, int) and num <=999:
        if num<1000 and num>99:
            num1= num % 10
            op1= num //10
            num2 = op1 % 10
            op2 = op1 //10
            num3 = op2
            return num3
    else: return "Error"

##            if num1 > num2 and num1 > num3:
##                return num1
##            if num2 > num1 and num2 > num3:
##                return num2
##            if num3 > num1 and num3> num2:
##                return num3
