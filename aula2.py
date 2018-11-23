import math

print('------------------')
print('Aula 2')
print('------------------')

print('\nExercício 01\n')          #valor das expressões

largura = 17
altura = 12.0
delimitador = "."

print(largura/2)      #8.5
print(largura/2.0)    #8.5
print(altura/3)       #4.0
print(1 + 2*5)        #11
print(delimitador*5)  #.....

print('\nExercício 02\n')         #calcular o volume de uma esfera de raio 5

r = 5                         #raio
v = (4*math.pi*(r**3))/3      #equação do volume

print('O volume da esfera de raio', r, 'é,', v)

print('\nExercício 03\n')         #custo total da compra de 60 livros

qts = 60                      #quantidade de livros
p = 24.95                     #preço de 1 livro
d = 0.4*p*qts                 #desconto na quantidade de livros
e = 3+(qts-1)*0.75            #custo total de envio
t = p*qts-d+e

print('O custo total para compra de', qts, 'livros é,', t, 'reais')

print('\nExercício 04\n')         #distância entre 2 cristas consecutivas

lmb = 632.8*(10**(-9))          #comprimento de onda
D = 1.98                      #distância do anteparo ate a fenda
d = 0.250*(10**(-3))            #tamanho da fenda
dy = (lmb*D)/d                #distância entre duas cristas consecutivas

print('A distância entre duas cristas consecutivas é', dy*(10**(3)), 'mm\n')