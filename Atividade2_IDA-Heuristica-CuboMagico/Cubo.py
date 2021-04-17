import random 

class Cubo:	
	def __init__(self):
		self.cubo = [0] * 54
		self.incializar_cubo()

	def incializar_cubo(self):
		for i in range(6):
			for j in range(9):
				cor_faceta = ''
				if i == 0:
					cor_faceta = 'W'
				elif i == 1:
					cor_faceta = 'O'
				elif i == 2:
					cor_faceta = 'G'
				elif i == 3:
					cor_faceta = 'R'
				elif i == 4:
					cor_faceta = 'B'
				elif i == 5:
					cor_faceta = 'Y'
				
				self.cubo[(i*9) + j] = cor_faceta

	def recuperar_cores(self, positions):
		def checa_cor(indice):
			return self.cubo[indice]

		def verificar_quina():
			return [
				checa_cor(positions[0]),
				checa_cor(positions[1]),
				checa_cor(positions[2])
			]
		def verificar_lado():
			return[
				checa_cor(positions[0]),
				checa_cor(positions[1])
			]

		def resposta():
			if len(positions) == 2:
				return verificar_lado()

			return verificar_quina()

		return resposta()

	def print_cubo(self):
		print(self.cubo)

	def frente_horario(self):
		temporario1 = self.cubo[6]
		self.cubo[6] = self.cubo[17]
		self.cubo[17] = self.cubo[47]
		self.cubo[47] = self.cubo[27]
		self.cubo[27] = temporario1

		temporario2 = self.cubo[7]
		self.cubo[7] = self.cubo[14]
		self.cubo[14] = self.cubo[46]
		self.cubo[46] = self.cubo[30]
		self.cubo[30] = temporario2

		temporario3 = self.cubo[8]
		self.cubo[8] = self.cubo[11]
		self.cubo[11] = self.cubo[45]
		self.cubo[45] = self.cubo[33]
		self.cubo[33] = temporario3

		temporario4 = self.cubo[18]
		self.cubo[18] = self.cubo[24]
		self.cubo[24] = self.cubo[26]
		self.cubo[26] = self.cubo[20]
		self.cubo[20] = temporario4

		temporario5 = self.cubo[19]
		self.cubo[19] = self.cubo[21]
		self.cubo[21] = self.cubo[25]
		self.cubo[25] = self.cubo[23]
		self.cubo[23] = temporario5

	def frente_anti_horario(self):
		self.frente_horario()
		self.frente_horario()
		self.frente_horario()

	def fundo_horario(self):
		temporario1   = self.cubo[0]
		self.cubo[0]  = self.cubo[29]
		self.cubo[29] = self.cubo[53]
		self.cubo[53] = self.cubo[15]
		self.cubo[15] = temporario1

		temporario2   = self.cubo[1]
		self.cubo[1]  = self.cubo[32]
		self.cubo[32] = self.cubo[52]
		self.cubo[52] = self.cubo[12]
		self.cubo[12] = temporario2

		temporario3   = self.cubo[2]
		self.cubo[2]  = self.cubo[35]
		self.cubo[35] = self.cubo[51]
		self.cubo[51] = self.cubo[9]
		self.cubo[9]  = temporario3

		temporario4   = self.cubo[36]
		self.cubo[36] =	self.cubo[42]
		self.cubo[42] = self.cubo[44]
		self.cubo[44] = self.cubo[38]
		self.cubo[38] = temporario4

		temporario5   = self.cubo[37]
		self.cubo[37] = self.cubo[39]
		self.cubo[39] = self.cubo[43]
		self.cubo[43] = self.cubo[41]
		self.cubo[41] = temporario5

	def fundo_anti_horario(self):
		self.fundo_horario()
		self.fundo_horario()
		self.fundo_horario()

	def esquerda_horario(self):
		temporario1   = self.cubo[0]
		self.cubo[0]  = self.cubo[44]
		self.cubo[44] = self.cubo[45]
		self.cubo[45] = self.cubo[18]
		self.cubo[18] = temporario1

		temporario2   = self.cubo[3]
		self.cubo[3]  = self.cubo[41]
		self.cubo[41] = self.cubo[48]
		self.cubo[48] = self.cubo[21]
		self.cubo[21] = temporario2

		temporario3   = self.cubo[6]
		self.cubo[6]  = self.cubo[38]
		self.cubo[38] = self.cubo[51]
		self.cubo[51] = self.cubo[24]
		self.cubo[24] = temporario3

		temporario4   = self.cubo[9]
		self.cubo[9]  = self.cubo[15]
		self.cubo[15] = self.cubo[17]
		self.cubo[17] = self.cubo[11]
		self.cubo[11] = temporario4

		temporario5   = self.cubo[10]
		self.cubo[10] = self.cubo[12]
		self.cubo[12] = self.cubo[16]
		self.cubo[16] = self.cubo[14]
		self.cubo[14] = temporario5

	def esquerda_anti_horario(self):
		self.esquerda_horario()
		self.esquerda_horario()
		self.esquerda_horario()

	def direita_horario(self):
		temporario1   = self.cubo[2]
		self.cubo[2]  = self.cubo[20]
		self.cubo[20] = self.cubo[47]
		self.cubo[47] = self.cubo[42]
		self.cubo[42] = temporario1

		temporario2   = self.cubo[5]
		self.cubo[5]  = self.cubo[23]
		self.cubo[23] = self.cubo[50]
		self.cubo[50] = self.cubo[39]
		self.cubo[39] = temporario2

		temporario3   = self.cubo[8]
		self.cubo[8]  = self.cubo[26]
		self.cubo[26] = self.cubo[53]
		self.cubo[53] = self.cubo[36]
		self.cubo[36] = temporario3

		temporario4   = self.cubo[27]
		self.cubo[27] = self.cubo[33]
		self.cubo[33] = self.cubo[35]
		self.cubo[35] = self.cubo[29]
		self.cubo[29] = temporario4

		temporario5   = self.cubo[28]
		self.cubo[28] = self.cubo[30]
		self.cubo[30] = self.cubo[34]
		self.cubo[34] = self.cubo[32]
		self.cubo[32] = temporario5


	def direita_anti_horario(self):
		self.direita_horario()
		self.direita_horario()
		self.direita_horario()


	def topo_horario(self):
		temporario1   = self.cubo[9]
		self.cubo[9]  = self.cubo[18]
		self.cubo[18] = self.cubo[27]
		self.cubo[27] = self.cubo[36]
		self.cubo[36] = temporario1

		temporario2   = self.cubo[10]
		self.cubo[10] = self.cubo[19]
		self.cubo[19] = self.cubo[28]
		self.cubo[28] = self.cubo[37]
		self.cubo[37] = temporario2

		temporario3   = self.cubo[11]
		self.cubo[11] = self.cubo[20]
		self.cubo[20] = self.cubo[29]
		self.cubo[29] = self.cubo[38]
		self.cubo[38] = temporario3

		temporario4   = self.cubo[0]
		self.cubo[0]  = self.cubo[6]
		self.cubo[6]  = self.cubo[8]
		self.cubo[8]  = self.cubo[2]
		self.cubo[2]  = temporario4

		temporario5   = self.cubo[1]
		self.cubo[1]  = self.cubo[3]
		self.cubo[3]  = self.cubo[7]
		self.cubo[7]  = self.cubo[5]
		self.cubo[5]  = temporario5

	def topo_anti_horario(self):
		self.topo_horario()
		self.topo_horario()
		self.topo_horario()


	def base_horario(self):
		temporario1   = self.cubo[15]
		self.cubo[15] = self.cubo[42]
		self.cubo[42] = self.cubo[33]
		self.cubo[33] = self.cubo[24]
		self.cubo[24] = temporario1

		temporario2   = self.cubo[16]
		self.cubo[16] = self.cubo[43]
		self.cubo[43] = self.cubo[34]
		self.cubo[34] = self.cubo[25]
		self.cubo[25] = temporario2

		temporario3   = self.cubo[17]
		self.cubo[17] = self.cubo[44]
		self.cubo[44] = self.cubo[35]
		self.cubo[35] = self.cubo[26]
		self.cubo[26] = temporario3

		temporario4   = self.cubo[45]
		self.cubo[45] = self.cubo[51]
		self.cubo[51] = self.cubo[53]
		self.cubo[53] = self.cubo[47]
		self.cubo[47] = temporario4

		temporario5   = self.cubo[46]
		self.cubo[46] = self.cubo[48]
		self.cubo[48] = self.cubo[52]
		self.cubo[52] = self.cubo[50]
		self.cubo[50] = temporario5

	def base_anti_horario(self):
		self.base_horario()
		self.base_horario()
		self.base_horario()



	def embaralhar_cubo(self):
		movimentos = [0] * 20
		movimentos = list (map(lambda x: random.randint(0, 12), movimentos))

		for movimento in movimentos:
			print(movimento)
			if movimento == 0:
				self.frente_horario()
			elif movimento == 1:
				self.frente_anti_horario()
			elif movimento == 2:
				self.fundo_horario()
			elif movimento == 3:
				self.fundo_anti_horario()
			elif movimento == 4:
				self.direita_horario()
			elif movimento == 5:
				self.direita_anti_horario()
			elif movimento == 6:
				self.esquerda_horario()
			elif movimento == 7:
				self.esquerda_anti_horario()
			elif movimento == 8:
				self.topo_horario()
			elif movimento == 9:
				self.topo_anti_horario()
			elif movimento == 10:
				self.base_horario()
			elif movimento == 11:
				self.base_anti_horario()


cubo = Cubo() 
cubo.print_cubo()
cubo.embaralhar_cubo()
cubo.print_cubo()
print(cubo.recuperar_cores([2,12]))
print(cubo.recuperar_cores([4,5,7]))