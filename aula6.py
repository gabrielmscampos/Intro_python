import turtle

cor = input('Qual cor do background você deseja? ')
cor_pato = input('Qual a cor que você deseja para a circunferência? ')
size_pato = int(input('Qual o tamanho dos desenhos? '))
speed_pato = int(input('Qual a velocidade de desenho das estrelas, de 0 a 10? '))
cores = ["yellow", "red", "purple", "blue", 'green']

jn = turtle.Screen()
jn.bgcolor(cor)
jn.title('ESTE É O PATÛNCIO')

pato = turtle.Turtle()
pato.color(cor_pato)
pato.pensize(size_pato)
pato.shape('turtle')
pato.speed(speed_pato)

pato2 = turtle.Turtle()
pato2.color(cor_pato)
pato2.pensize(size_pato)
pato2.shape('turtle')
pato2.speed(speed_pato)

pato3 = turtle.Turtle()
pato3.color(cor_pato)
pato3.pensize(size_pato)
pato3.shape('turtle')
pato3.speed(speed_pato)

pato4 = turtle.Turtle()
pato4.color(cor_pato)
pato4.pensize(size_pato)
pato4.shape('turtle')
pato4.speed(speed_pato)

pato5 = turtle.Turtle()
pato5.color(cor_pato)
pato5.pensize(size_pato)
pato5.shape('turtle')
pato5.speed('fastest')

pato2.penup()
pato3.penup()
pato4.penup()
pato5.penup()

pato2.forward(180)
pato3.left(90)
pato3.forward(180)
pato3.right(90)
pato4.left(90)
pato4.forward(180)
pato4.right(90)
pato4.forward(180)
pato5.backward(180)

pato2.pendown()
pato3.pendown()
pato4.pendown()
pato5.pendown()

for i in cores:
	pato.color(i)
	pato2.color(i)
	pato3.color(i)
	pato4.color(i)
	pato.forward(144)
	pato2.forward(144)
	pato3.forward(144)
	pato4.forward(144)
	pato.right(144)
	pato2.right(144)
	pato3.right(144)
	pato4.right(144)

for i in range(0,360):
	pato5.forward(1)
	pato5.left(1)

jn.mainloop()