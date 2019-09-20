
# Ejercicio 1
class Empleado:
    def __init__(self, numero, nombre, salario):
        self.numero  = numero
        self.nombre = nombre
        self.salario = salario

    def get_numero(self):
        return self.numero
    def set_numero(self,nuevo1):
        self.numero = nuevo1

    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nuevo2):
        self.nombre = nuevo2
        
    def get_Salario(self):
        return self.salario
    def set_Salario(self,nuevo3):
        self.salario = nuevo3

    def mostrar(self):
        print(" Numeros" + str(self.get_numero()))
        print(" Nombres" + self.get_nombre())
        print(" Salario" + str(self.get_Salario()))
        print("__"*15)

    def calculo_salario(self,horas):
        if isinstance(horas,int):
            return horas*self.get_Salario()

E = Empleado

empleado = [Empleado(1,"Pepe",7000),Empleado(2,"Vegeta777", 2520),Empleado(3,"Satan",80000),Empleado(4,"Yung Gravy",5620),Empleado(5,"Juan",1250)]

def obtener(lista):
    if lista == []:
        return None
    elif lista[0].calculo_salario(1) > 5000:
        lista[0].mostar()
        return obtener(lista[1:])
    else:
        return obtener(lista[1:])
    
# Ejercicio 2

class Uber:
    def __init__(self, placa,marca,año,estado,tipo,viajes_realizados,monto_actual,acumulado):
        self.placa = placa
        self.marca = marca
        self.año = año
        self.tipo = tipo
        self.viajes_realizados = viajes_realizados
        self.monto_actual = monto_actual
        self.acumulado = acumulado

    def get_placa(self):
        return self.placa
    def set_placa(self,nuevo):
        self.placa = nuevo
        
    def get_marca(self):
        return self.marca
    def set_marca(self,nuevo2):
        self.marca = nuevo2

    def get_año(self):
        return self.año
    def set_año(self,nuevo3):
        self.año = nuevo2

    def get_estado(self):
        return self.estado
    def set_estado(self,nuevo4):
        self.estado = nuevo4
        
    def get_tipo(self):
        return self.tipo
    def set_tipo(self,nuevo5):
        self.tipo = nuevo5

    def get_viajes_realizados(self):
        return self.viajes_realizados
    def set_viajes_realizados(self,nuevo6):
        self.viajes_realizados = nuevo6

    def get_monto(self):
        return self.monto_actual
    def set_monto(self,nuevo7):
        self.monto_actual = nuevo7

    def get_acumulado(self):
        return self.acumulado
    def set_acumulado(self,nuevo8):
        self.acumulado = nuevo8

    # Set
    def setViaje(self,nuevo9):
        self.cantidad = nuevo9
    def defViaje (self,nuevo10):
        return self,viaje
    
    def setEstado(self,nuevo10):
        return self.estado == nuevo10

    # Notificar
    def mostar(self):
        print( self.placa)
        print( self.marca)
        print( self.año)
        print( self.estado)
        print( self.tipo)
        print( self.viajes_realizados)
        print( self.monto)
        print( self.acumulado)
        
    def rest(self):
        return setViajes(0)

    def enviar_reparacion(self):
        return setEstado("Reparacion")
    def recibir_reparacion(self):
        return setEstado ("Libre")
    
    def viaje (kilometros):
        if self.tipo == "Premium":
            return self.setviajes(1) and setMonto (kilometros * 500)
        elif self.tipo == "economicos":
            return self.setViajes(1), setMonto(kilometros*300)
