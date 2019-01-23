print('----------------')
print('Aula 10')
print('----------------')

print('\n----------------')
print('Exercício 1')
print('----------------')

def dobrar_elementos(uma_lista):
    """ Cria uma nova_lista com o dobro dos valores dos elementos de uma_lista
    """
    nova_lista = []
    for (i, valor) in enumerate(uma_lista):
        novo_elem = 2 * valor
        nova_lista.append(novo_elem)

    return nova_lista

minha_lista = [2, 4, 6]
print('Lista inicial:', minha_lista)
nova_lista = dobrar_elementos(minha_lista)
print('A nova lista é:', nova_lista)

print('\n----------------')
print('Exercício 2')
print('----------------')

lista = []
for i in range(0,10000):
	lista.append(i+1)

print(lista)

print('\n----------------')
print('Exercício 3')
print('----------------')

def prim_int_positivo(n):
	a_lista = []
	for i in range(101,n):
		a_lista.append(i)
		if i % 21 == 0:
			return i

n = int(input('Digite um número n maior que 101: '))
x = prim_int_positivo(n)
print('O primeiro número divísivel por 21 entre 101 e', n-1, 'é:', x)

print('\n----------------')
print('Exercício 4')
print('----------------')

η_0 = [-1,0,0,0]
η_1 = [0,1,0,0]
η_2 = [0,0,1,0]
η_3 = [0,0,0,1]

η = [η_0,η_1,η_2,η_3]

print('η =', η)
print('O elemento η{3,3} é:', η[3][3])