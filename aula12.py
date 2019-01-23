print('----------------')
print('Aula 12')
print('----------------')

print('\n----------------')
print('Exercício 1')
print('----------------')

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3, (2,2): 0}

print('O elemento {0,3} da matriz é:', matrix.get((0,3)))
print('O elemento {2,1} da matriz é:', matrix.get((2,1)))
print('O elemento {4,3} da matriz é:', matrix.get((4,3)))
print('O elemento {2,2} da matriz é:', matrix.get((2,2)))

print('\n----------------')
print('Exercício 2')
print('----------------')
print('a)')

def tabela_de_frequencia(palavra):
	count_letras = {}
	for i in palavra:
		count_letras[i] = count_letras.get(i, 0) + 1
	return count_letras

palavra = input('Digite a palavra que você deseja imprimir uma tabela de frequência: ')
dicti = tabela_de_frequencia(palavra)
print(dicti)

print('\nb)')

def ordenação(dicti):
	dicti = list(dicti.items())
	dicti.sort()
	return dicti

print(ordenação(dicti))

print('\n----------------')
print('Exercício 3')
print('----------------')

def tabela_ordenada(palavra):
	count = {}
	for i in palavra:
		count[i] = count.get(i,0) + 1
	return count

palavra = input('Digite a string que você deseja ordenar em uma tabela de frequência: ')
palavra = "".join(palavra.strip(".").split()).lower()
dicti = tabela_ordenada(palavra)

for (i,j) in sorted(dicti.items()):
	print(i,j)