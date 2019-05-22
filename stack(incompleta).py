class Pila:
	def __init__(self):
		self.__pi = [ ]

	def len(self):
		return len(self.__pi)

	def is_empty(self):
		return len(self.__pi) == 0

	def push(self,e):
		self.__pi.append(e)

	def top(self):
		if self.is_empty():
			raise MiGatito("Stack is empty")
		else: return self.__pi[-1]

	def pop(self):
		if self.is_empty():
			raise MiGatito("Srack is empty")
		else: return self.__pi.pop()

	def test(self):
		try:
			self.Stack = Pila()
			self.Stack.push(5)