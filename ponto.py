class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return (self.x**2 + self.y**2)**0.5

    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto(mx, my)

    def distancia_entre_pontos(self, alvo):
    	""" Calcula a distância entre um ponto e outro ponto alvo """
    	dx = (alvo.x - self.x)**2
    	dy = (alvo.y - self.y)**2
    	return (dx + dy)**0.5

    def reflexao_x(self):
    	""" Calcula o ponto refletido pelo eixo x """
    	return Ponto(self.x,-(self.y))

    def inclinacao_da_origem(self):
    	""" Calcula o ângulo entre a origem e o ponto """
    	if self.x == 0:
    		return None
    	else:
    		return self.y/self.x

    def coeficiente_angular(self,alvo):
    	""" Calcula o coeficiente angualr entre dois pontos """
    	if (alvo.x - self.x) == 0:
    		return None
    	else:
    		return (alvo.y - self.y)/(alvo.x - self.x)

    def equaçao_da_reta(self,alvo):
    	""" Calcula a equação da reta entre um ponto e outro ponto alvo """
    	m = self.coeficiente_angular(alvo)
    	n = self.y - m*self.x
    	return (m, n)

if __name__ == '__main__':
	px, py = eval(input('Digite as coordenadas (x,y) do ponto p: '))
	print('O ponto p é:', Ponto(px, py))