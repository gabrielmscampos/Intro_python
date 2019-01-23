print('\n----------')
print('Aula 16')
print('----------')

from math import *

print('\n--------------------')
print('Exercício 1, 2, 3 e 4')
print('--------------------')

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

px, py = eval(input('Digite as coordenadas (x,y) do ponto p: '))
qx, qy = eval(input('Digite as coordenadas (x,y) do ponto q alvo: '))

m, n = Ponto(px, py).equaçao_da_reta(Ponto(qx, qy))

print('\nO ponto p é:', Ponto(px, py))
print('O ponto q é:', Ponto(qx, qy))
print('A distância entre p e a origem é:', Ponto(px, py).distancia_da_origem(), 'unidades de medida.')
print('A distância entre q e a origem é:', Ponto(qx, qy).distancia_da_origem(), 'unidades de medida.')
print('O ponto médio entre p e q é:', Ponto(px, py).ponto_medio(Ponto(qx, qy)))
print('A distância entre os pontos p e q é:', Ponto(px, py).distancia_entre_pontos(Ponto(qx, qy)), 'unidades de medida.')
print('A reflexão do ponto p pelo eixo x é:', Ponto(px, py).reflexao_x())
print('A inclinação da reta que une os pontos', Ponto(px, py), 'é:', Ponto(px, py).inclinacao_da_origem())
print('O programa pode dar errado caso a coordenada x do ponto seja 0, pois, não há divisão por 0, por isso, é preciso adicionar um if statement que retorne None caso self.x = 0.')
print('O coeficiente angular e linear da reta formada pelos pontos', Ponto(px, py), 'e', Ponto(qx, qy), 'é', Ponto(px, py).equaçao_da_reta(Ponto(qx, qy)))
print('A equação geral da reta entre', Ponto(px, py), 'e', Ponto(qx, qy), 'é: y =', m, 'x +', n)
print('O método falha quando a subtração das coordenadas x de cada ponto é igual 0, como não há divisão por zero é necessário implementar um if statement que retorne None caso alvo.x - self.x = 0.')