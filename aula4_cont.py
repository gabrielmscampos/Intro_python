print('-----------')
print('Aula 4_cont')
print('-----------')

from math import *

print('\nExercício 1')

import time
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8') #locale -a no terminal para ver os locais instalados na máquina

def hoje(): #Função para informar a data e horário do momento que a função foi chamada
	t = time.localtime() #quando o argumento é None retorna o tempo atual segundo time()
	print(time.strftime('Hoje é %A, %d de %B de %Y às %H:%M:%S', t))

hoje()

#time.localtime(secs) converte o epoch time em segundos para uma 9-tuple de class.struct_time do tempo convertido
#time.localtime(0) retorna a 9-tupla (1969, 12, 31, 21, 1, 30, 2, 365, 0) onde temos (ano, mês, dia, horas, minutos, segundos, weekday, yearday, dst)
#time.strftime('format', t) converte o time structure gerado em t para um formato (string).

#def conta(n):
	#for i in range(n): #range(n): cria uma lista 0,1,2,3,...,n-1
		#result = n*i #i pega o utlimo número da lista, ou seja, n-1
	#return result

#print(conta(1))

print('\nExercício 2: fatorial')

def fatorial(n):
	x = 1 #Sem isso aparece UnboundLocalError: local variable 'x' referenced before assignment
	for i in range(1, n+1): #range(1, 5) cria a lista 1,2,3,4, portando, range(1,n+1) cria a lista 1,2,3,...,n
		x = x*i
	return x

n = int(input('Digite um número inteiro maior do que 0 para calcular o fatorial: '))
print('O fatorial de', n, 'é', fatorial(n))

print('\nExercício 2: fatorial recursivo')

def factorial(k):
	if k == 0:
		return 1
	else:
		return k*factorial(k-1)

k = int(input('Digite um número inteiro positivo para calcular o fatorial: '))
print('O fatorial de', k, 'é', factorial(k))

print('\nExercício 3: comparação')

def comp(x,y):
	if x > y:
		print('O maior número é:', x)
	elif y > x:
		print ('O maior número é:', y)

x = eval(input('Digite o primeiro número: '))
y = eval(input('Digite o segundo número: '))
comp(x,y)

print('\nExercício 3: comparação tuple')

def comp_tuple(x,y):
	if x > y:
		tuple = (x,y)
		print('A ordem da esquerda para direita representa o maior número:', tuple)
	elif y > x:
		tuple = (y,x)
		print('A ordem da esquerda para direita representa o maior número:', tuple, '\n')

x = eval(input('Digite o primeiro número: '))
y = eval(input('Digite o segundo número: '))
comp_tuple(x,y)