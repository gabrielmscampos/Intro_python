import turtle
import math

# Função que desenha um arco de circunferência
def desenhar_arco(turtle, raio, angulo):
    arc_length = 2*math.pi*raio*(angulo/360)
    lados = int(arc_length/3) + 1
    step_length = arc_length/lados
    step_angle = angulo/lados

    for i in range(lados):
        turtle.forward(step_length)
        turtle.left(step_angle)

#  Função que desenha as petalas usando a função de arco
def desenhar_petala(turtle, raio, angulo):
    desenhar_arco(turtle, raio, angulo)
    turtle.left(180-angulo)
    desenhar_arco(turtle, raio, angulo)
    turtle.left(180-angulo)

# Função para desenhar o cabo da flor
def talo(comprimento,cor):
    turtle.color(cor)
    turtle.setheading(270)         # O setheading(270) seta a orientação da tartaruga para o SUL (https://docs.python.org/3/library/turtle.html#turtle.setheading)
    turtle.forward(comprimento)
    turtle.hideturtle()

# Função para desenhar as folhas da flor
def folhas(turtle,cor):
    turtle.color(cor)
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(0,2):
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(30)
        turtle.right(150)
    turtle.end_fill()

# Função que çompoe todo o desenho a partir das funções acima
def desenhar_flor(turtle, petalas, raio, angulo):
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for j in range(petalas):
        desenhar_petala(turtle, raio, angulo)
        turtle.left(360/petalas)
    turtle.end_fill()

    talo(160,'green')

    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    folhas(turtle, 'green')
    turtle.left(180)
    folhas(turtle, 'green')
    turtle.left(270)
    turtle.hideturtle()

petalas = int(input('\nQual o número de petalas da flor? ')) # Pergunta ao usuário o número de petalas

janela = turtle.Screen()
zeca = turtle.Turtle()
zeca.shape("turtle")
zeca.speed(0)

desenhar_flor(zeca, petalas, 100, 40)
janela.mainloop()