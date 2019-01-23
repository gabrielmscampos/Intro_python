print('\n----------')
print('Aula 17')
print('----------')

from math import *
from ponto import *
import turtle

print('\n----------------')
print('Exercício 1')
print('----------------')

class Rectangle:
    """Representa um retangulo. 

    atributos: 
    - largura, do tipo float
    - altura, do tipo float 
    - canto, do tipo Ponto.
    """

    def __init__(self,largura,altura,canto):
    	self.largura = largura
    	self.altura = altura

    	if not isinstance(canto, Ponto):
    		raise TypeError('O canto deve ser um Ponto.')
    	else:
    		self.canto = canto

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.largura, self.altura, self.canto)

a = Ponto(3,2)
#retangulo = Rectangle(1,2,4) # TypeError: O canto deve ser um Ponto.
rect = Rectangle(1,2,a)
print('A largura do retângulo é', rect.largura)
print('A altura do retângulo é', rect.altura)
print('O canto o retângulo está localizado no ponto', a)

print('\n----------------')
print('Exercício 2')
print('----------------')

class Circulo:
	""" Representa um circulo.
	Atributos:
	- raio, do tipo float
	- centro, do tipo Ponto.
	"""

	def __init__(self,raio,centro):
		self.raio = raio

		if not isinstance(centro, Ponto):
			raise TypeError('O centro deve ser um ponto.')
		else:
			self.centro = centro

	def __str__(self):
		return "({0}, {1})".format(self.raio, self.centro)

	def ponto_no_circulo(self,alvo):
		""" Verifica se um ponto alvo está dentro do circulo """
		dx = (alvo.x - self.centro.x)**2
		dy = (alvo.y - self.centro.y)**2
		d = (dx + dy)**0.5
		if d <= self.raio:
			return True
		else:
			return False

o = Ponto(150,100)
circ = Circulo(75,o)
p = Ponto(120,120)

print('As coordenadas x,y do centro do círculo são', o)
print('O ponto', p, 'está contido no círculo', circ, '?', circ.ponto_no_circulo(p))

print('\n----------------')
print('Exercício 3 e 4')
print('----------------')

def desenhar_ret(turt,rect):
	jn = turtle.Screen()
	jn.bgcolor('white')
	jn.title('Retângulos')

	turt.color('black')
	turt.pensize('3')
	turt.shape('turtle')
	turt.speed(1)

	turt.penup()
	turt.setposition(rect.canto.x,rect.canto.y)
	turt.pendown()
	turt.write('  ' + str(rect.canto))

	for i in range(2):
		turt.left(90)
		turt.forward(rect.largura)
		turt.left(90)
		turt.forward(rect.altura)

	turt.hideturtle()
	jn.exitonclick()

def desenhar_circulo(turt,circ):
	wn = turtle.Screen()
	wn.bgcolor('white')
	wn.title('Círculos')

	turt.color('black')
	turt.pensize('3')
	turt.shape('turtle')
	turt.speed(0)

	turt.penup()
	turt.setposition(circ.centro.x,circ.centro.y)
	turt.pendown()
	turt.write(circ.centro, align = 'center')
	turt.forward(circ.raio)
	turt.write('  ' + str(circ.raio) + ' u.m')
	turt.right(90)

	perimetro = 2*pi*circ.raio

	for i in range(0,360):
		turt.forward(perimetro/360.0)
		turt.right(1)

	turt.hideturtle()
	wn.exitonclick()

ask = input('Você deseja desenhar o retângulo, ou o círculo? [rect/circ] ')
while ask not in {'rect', 'circ'}:
	print('Essa não é uma resposta válida!')
	ask = input('Você deseja desenhar o retângulo ou o círculo? [rect/circ] ')

if ask == 'rect':
	b = Ponto(100,-40)
	rect = Rectangle(120,50,b)
	turt = turtle.Turtle()
	desenhar_ret(turt,rect)
else:
	o = Ponto(-30,6)
	circ = Circulo(30,o)
	turt = turtle.Turtle()
	desenhar_circulo(turt,circ)