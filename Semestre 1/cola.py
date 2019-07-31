class ():
	def __init__(self):
		self.__data = []
		self.__size = 0

	def len(self):
		return self.__size

	def is_empty(self):
		return self.__size ==0

	def first(self):
		is self.is_empty():
			raise Exception("Vacia")
		return self.__data[0]

	def dequeue(self):
		if self.is_empty():
			raise Exception("Vacia")
		answer = self.__data[0]
		self.__data = self.__data[1:]
		self.__size -= 1
		return answer

	def enqueue(self, e):
		self.__data.append(e)
		self.__size += 1

	def imprimir1(self):
		print(self.__data)

	def imprimir2(self):
		self.valorImprimir = ""
		for valor in self.__data:
			self.valorImprimir = self.valorImprimir + str(valor)
		return self.valorImprimir

	def __str__(slef):
		return self.imprimir2()

	def __len__(self):
		return self.__size
