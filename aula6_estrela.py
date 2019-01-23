import turtle

def desenhar_estrela(num_pontas, cor, tamanho):
	zeca = turtle.Turtle()
	zeca.color(cor)

	zeca.penup()
	zeca.goto(x,y)
	zeca.pendown()

	angulo = 0
	if num_pontas % 2 == 0:              # estrela com número de pontas par
		angulo = 180 - (360/num_pontas)
		if num_pontas % 4 != 0:
			print('O programa não suporta estrela com número de pontas do tipo n = 2*num_ímpar')
			print('Será desenhada uma esterla de n = ', int(num_pontas/2), 'pontas, 2 vezes')

	else:                                # estrela com número de pontas ímpares
		angulo = 180 - (180/num_pontas)

	for i in range(num_pontas):
		zeca.forward(tamanho)
		zeca.left(angulo)

	zeca.penup()
	zeca.hideturtle()
	return

def __main__():
	board = turtle.Screen()
	board.bgcolor('blue')
	board.title('Exercício')

	desenhar_estrela(num_pontas, cor, tamanho)

	board.mainloop()

num_pontas = int(input('\nQuantas pontas a estrela deve ter? '))
if num_pontas <= 4:
	raise SystemExit('Não a pontas suficientes para desenhar uma estrela')

cor = input('Qual a cor que você quer para o desenho? ')
tamanho = int(input('Qual o tamanho que você quer para estrela (é preferível um número > 50): '))
x,y = eval(input('Qual as coordenadas inicais do desenho (x,y): '))

__main__()