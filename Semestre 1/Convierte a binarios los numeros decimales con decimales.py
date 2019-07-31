#Convierte a binarios los numeros decimales con decimales.
#JAJAJA xD

def decimal_fracciones(numero):
    if isinstance(numero, float):
        return(decimal_binario_aux(int(numero)), fraccion_binario_aux(numero - int(numero)))
    else: return "El valor no es un numero real"

def decimal_binario_aux(decimal):
    if decimal == 0: #rojo
        return []
    else: return decimal_binario_aux(decimal // 2) + (deciaml % 2) #verde

def fraccion_binario_aux(fraccion):
    if fraccion == 0.0: #rojo
        return[]
    else: return([ int(fraciion * 2)] + fraccion_binario_aux((fraccion * 2)-int(fraccion * 2)))
