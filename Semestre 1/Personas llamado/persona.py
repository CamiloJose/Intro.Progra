class persona:
	def __init__(self, nombre, cedula, edad):
		self.x = 0
		self.__nombre  = nombre
		self.__cedula = cedula
		self.__edad = edad

	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, nombre):
		if isinstance (nombre, str):
			self.__nombre = nombre
		else: return "El nombre no es string"

	@property
	def cedula(self):
		return self.__cedula = cedula
	@cedula.setter
	def cedula(self,cedula):
		if isinstance(cedula, int):
			return self.__cedula = cedula
		else: return "La cedula no es numero"

	@property
	def edad(self):
		return self.__edad
	@edad.setter
	def edad (self,edad):
		if (isinstance(edad, int)):
			self.__edad = edad
		else: print("Valor no es numero")
