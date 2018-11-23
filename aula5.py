print('------')
print('Aula 5')
print('------')

from math import pi
from math import e

print('\nExercício 1')

def valormax(x,y,z):
	lista = [x, y, z]

	if x > y and x > z:
		print ('\nO maior número entre os três é: ', x)
	elif y > x and y > z:
		print ('\nO maior número entre os três é: ', y)
	elif z > x and z > y:
		print ('\nO maior número entre os três é: ', z)

x = eval(input('Digite o primeiro valor da lista: '))
y = eval(input('Digite o segundo valor da lista: '))
z = eval(input('Digite o terceiro valor da lista: '))
valormax(x,y,z)
	
print('\nExercício 2')

def soma_lista(n):
	lista = []
	for i in range(n):
		print('Elemento (', i,'): ', end='')
		x = eval(input())
		lista.append(x)

	soma = 0
	for element in lista:
		soma = soma + element
	return soma

n = int(input('Digite o tamanho da lista: '))
print('\nA soma de todos os números da lista é:', soma_lista(n))

print('\nExercício 3')

def prod_lista(k):
	lista = []
	for i in range(k):
		print('Elemento (', i,'): ', end='')
		x = eval(input())
		lista.append(x)

	prod = 1
	for element in lista:
		prod = prod*element
	return prod

k = int(input('Digite o tamanho da lista: '))
print('\nA multiplicação de todos números da lista é:', prod_lista(k))

print('\nExercício 4')

def intervalo(a,b,num):
	if num <= b and num >= a:
		print('\nO número está dentro do intervalo.')
	else:
		print('\nO número está fora do intervalo.')

a = eval(input('Digite o limite inferior do intervalo: '))
b = eval(input('Digite o limite superior do intervalo: '))
num = eval(input('Digite o número que você deseja verificar se está contido no intervalo: '))
intervalo(a,b,num)

print('\nExercício 5')

def pares_lista(c):
	lista = []
	for i in range(c):
		print('Elemento (', i,'): ', end='')
		x = eval(input())
		lista.append(x)

	lista_pares = []
	for element in lista:
		y = element%2
		if y == 0:
			lista_pares.append(element)

	print('\nOs pares são,', lista_pares)

c = int(input('Digite o tamanho da lista: '))
pares_lista(c)

print('\nExercício 6')
	
print('\nExercício 6')
	
def num_perfeito(u):
	lista_divisores = []
	for i in range(1, u+1):
			x = u%i
			if x == 0:
				lista_divisores.append(i)

	soma_divisores = 0
	for element in lista_divisores:
		soma_divisores = soma_divisores + element

	if soma_divisores/2 == u:
		print('O número', u,'é perfeito.\n')
	else:
		print('O número', u,'não é perfeito.\n')

u = eval(input('Digite o número que você deseja verificar se é perfeito: '))
num_perfeito(u)