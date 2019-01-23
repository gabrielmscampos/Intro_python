import turtle
def draw_bar(t, altura, comprimento):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(altura)
    t.write(str(altura))
    t.right(90)
    t.forward(comprimento)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()             # Added this line

back_color = input('\nEscolha uma cor para o background: ')
line_color = input('Escolha uma cor para os traços do histograma: ')
fill_color = input('Escolha uma cor para preencher o histograma: ')
n = int(input('\nDigite a quantidade de dados que seu histograma deve ter: '))

dado = []
for i in range(1, n+1):
    print('Dado (',i,'): ', end='')
    y = eval(input())
    dado.append(y)

freq = []
for j in range(1, n+1):
    print('Frequência do dado (',j,'): ', end='')
    x = eval(input())
    freq.append(x)

if type(dado) == list:
    if type (freq) == list:
        wn = turtle.Screen()         # Set up the window and its attributes
        wn.bgcolor(back_color)

        tess = turtle.Turtle()       # Create tess and set some attributes
        tess.color(line_color, fill_color)
        tess.pensize(2)

        for a,b in zip(dado,freq):
                draw_bar(tess, a, b)

        wn.mainloop()
else:
    raise SystemExist('Os dados devem ser armazenados em listas. Encerrando o programa.')
