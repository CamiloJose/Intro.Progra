class Clinica:
	def __init__(self):
		self.dict = {}

	def agregarMedico(self, medicto):
		self.dict[medico] = Cola()

	def actualizarMedico(self, medico, cola):
		self.dict[medico] = cola

	def regristrarPaciente(self, medico, paciente):
		mCola = self.dict[medico] 			 #Saca cola de pacientes del medico
		mCola.enqueue(paciente)				 # Ingresa un nuevo paciente
		self.actualizarMedico(medico, mCola) #Actualiza la cola de pacientes del medico

	def siguientes(self, medico):
		mCola = self.dict[medico] #Saca cola de pacientes del medico
		print("Imprimir cola: ", mCola)
		paciente = mCola.dequeue() # Saca el siguiente paciente en la cola
		self.actualizarMedico(medico, mCola) #Actualiza la cola de pacientes del medico
		return paciente

	def test(self):
		cola = Cola() #Define medico y cola
		cola.enqueue("Pedro")# Ingresa un paciente en la cola de Pablo
		cola.enqueue("Marco")# Ingresa un paciente en la cola de Pablo
		self.agregarMedico("Pablo", cola) #Ingresa a pablo y su cola de pacientes
		mCola = self.dict["Pablo"] #Saca cola de pacienes de pablo
		print(mCola.dequeue())#saca el siguiente paciente en la cola
		print(mCola.dequeue())#saca el siguiente paciente en la cola
		cola1 = Cola() #//
		cola1.enqueue("P")
		cola1.enqueue("M")
		self.agregarCola("Jose", cola1)
		mCola = self.dict["Jose"] # //
		print(mCola.dequeue())
		print(mCola.dequeue())
