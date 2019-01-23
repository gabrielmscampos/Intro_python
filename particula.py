"""
#----------------------------------------------------------------------------------
# Projeto 2 - Cinemática de colisões relativísticas (Aniquilação elétron-pósitron)
# Aluno: Gabriel Moreira e Victor Augustus
# Professoras: Helena Malbouisson e Clemencia Mora
# Disciplina: Introdução a Python - UERJ 2018.2
#----------------------------------------------------------------------------------

Esse script foi desenvolvido para criar uma classe base de 4-vetor para representação de partículas.
"""

class vec4():
	""" Cria um objeto 4-vetor """

	def __init__(self, u0 = 0, un = 0):
		""" Inicializa um novo 4-vetor com atributos u0, un """
		self.u0 = u0
		self.un = un

	def __str__(self):
		""" Facilita o print dos atributos do 4-vetor """
		return '({0}, {1})'.format(self.u0, self.un)

	def __add__(self,alvo):
		""" Soma de 4-vetor """
		return vec4(self.u0 + alvo.u0, self.un + alvo.un)

	def __sub__(self,alvo):
		""" Subtração de 4-vetor """
		return vec4(self.u0 - alvo.u0, self.n1 - alvo.n1)

	def __mul__(self,alvo):
		""" Produto escalar entre dois 4-vetor ou produto de 4-vetor por um escalar """
		if isinstance(alvo,vec4):
			return self.u0*alvo.u0 + self.un*alvo.un
		else:
			try:
				return vec4(alvo*self.u0, alvo*self.un)
			except:
				return None

	def __rmul__(self,alvo):
		""" Produto de 4-vetor por um escalar """
		return vec4(alvo*self.u0, alvo*self.un)

	def __truediv__(self,alvo):
		""" Divisão de 4-vetor por um escalar """
		if isinstance(alvo,vec4):
			return 'Não há divisão entre quadri-vetores.'
		else:
			return vec4(self.u0/alvo, self.un/alvo)

	def __mod__(self,alvo):
		""" Resto da divisão de cada componente do 4-vetor por um escala """
		if isinstance(alvo,vec4):
			return 'Não há divisão entre quadri-vetores.'
		else:
			return vec4(self.u0%alvo, self.un%alvo)

	def __neg__(self):
		""" Troca o sinal das componente do 4-vetor """
		return vec4(-self.u0, -self.un)

	def __abs__(self):
		""" Calcula o módulo do 4-vetor """
		return sqrt(self.u0**2 + self.un**2)

class Particula(vec4):
	""" Cria um objeto particula """

	def __init__(self, m = 0, p = 0):
		""" Inicializa uma partícula com atributos de massa e momentum relativístico"""
		vec4.__init__(self, m, p)

	def momentum4(self):
		""" Calcula o 4-vetor momentum relativístico da particula """
		return vec4(self.energia(), self.un)

	def energia(self):
		""" Calcula a energia relativística da particula """
		return ((self.u0)**2 + (self.un)**2)**0.5

if __name__ == '__main__':
	e = Particula(0.511)
	p = Particula(0.511,30)
	print(e.energia(), e.momentum4())
	print(p.energia(), p.momentum4())