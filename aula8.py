print('----------------')
print('Aula 8')
print('----------------')

print('\n----------------')
print('Exercício 1')
print('----------------')

def regras_collatz(n):
	if n % 2 == 0:
		n = n/2
	else:
		n = 3*n + 1
	return n

print('A conjecture de Collatz, diz que: "Todos os inteiros positivos irão eventualmente convergir para 1 usando as regras do Collatz"')
n = int(input('\nDigite um número inteiro n > 0 para testar a conjecutra de Collatz: '))

while n < 0 or n == 0 or n == 1:
	if n < 0:
		print('O número', n, 'não pode ser utilizado.')
		n = int(input('Digite um número inteiro n > 0 para testar a conjecutra de Collatz: '))
	elif n == 0:
		print('O número 0 não pode ser utilizado.')
		n = int(input('Digite um número inteiro n para testar a conjecutra de Collatz: '))
	elif n == 1:
		print('O número 1 não pode ser utilizado.')
		n = int(input('Digite um número inteiro n para testar a conjecutra de Collatz: '))		

seq = [n]
contador = 0
while n != 1:
	contador = contador + 1
	n = regras_collatz(n)
	seq.append(n)

print('\nA sequêcia de Collatz é:', seq)
print('A quantidade de regras de Collatz utilizadas foi:', contador)

print('\n----------------')
print('Exercício 2')
print('----------------')

def count_0_e_5(n):
	count0 = 0
	count5 = 0
	for i in n:
		if i == "0":
			count0 = count0 + 1
		elif i == "5":
			count5 = count5 + 1
	return count0, count5

n = input('Digite o número que você deseja verificar a quantidade de zeros e cincos: ')
count0, count5 = count_0_e_5(n)
print('O número número', n, 'tem', count0, 'zeros e', count5, 'cincos.')

print('\n----------------')
print('Exercício 3')
print('----------------')

def print_until_k(list,k):
	if k == 'par':
		for i in list:
			if i % 2 == 0:
				break
			print(i)
		print('Done')
	elif k == 'ímpar':
		for i in list:
			if i % 2 == 1:
				break
			print(i)
		print('Done')

n = int(input('Digite a quantidade de elementos que sua lista deve ter: '))

lista = []
for i in range(1, n+1):
    print('Elemento (',i,'): ', end='')
    x = eval(input())
    lista.append(x)

k = input('Você deseja que o loop pare no primeiro número par ou ímpar de sua lista? ')
print_until_k(lista,k)

print('\n----------------')
print('Exercício 4')
print('----------------')

def sqrt_newton(n):
    approx = n/2.0
    count = 0
    while True:
    	count = count + 1
    	melhor = (approx + n/approx)/2.0
    	if abs(approx - melhor) == 0:
    		return melhor, count
    	approx = melhor

n = int(input('Digite o número que você deseja saber a raiz quadrada: '))
sqrt, count = sqrt_newton(n)

print('A raiz quadrada de', n, 'é:', sqrt)
print('Foram necessárias', count, 'iterações para calcular essa raiz quadrada.')