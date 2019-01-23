print('\n----------')
print('Aula 13')
print('----------')

import matplotlib.pyplot as plt
import os
import aula13_wc as wc

print('\n----------------')
print('Exercício 1')
print('----------------')

def histrograma(data,freq,title,x_label,y_label):
	plt.bar(data,freq)
	plt.suptitle(title, fontsize = 14)
	plt.xlabel(x_label, fontsize = 12)
	plt.ylabel(y_label, fontsize = 12)
	plt.show()

def dados_alunos_histrogramas(arquivo):
	try:
		file = open(arquivo)
	except:
		print('O arquivo dados_alunos.txt não foi encontrado.')
		print('Encerrando o programa.')

	objeto = file.readlines()
	open(arquivo).close()

	coluna_0 = []
	coluna_1 = []
	coluna_2 = []
	for i in objeto:
		column = i.strip().split('\t')
		coluna_0.append(eval(column[0]))
		coluna_1.append(eval(column[1]))
		coluna_2.append(eval(column[2]))

	freq_0 = []
	data_0 = []
	for j in coluna_0:
		if j not in data_0:
			data_0.append(j)

	for k in data_0:
		freq_0.append(coluna_0.count(k))

	freq_1 = []
	data_1 = []
	for j in coluna_1:
		if j not in data_1:
			data_1.append(j)

	for k in data_1:
		freq_1.append(coluna_1.count(k))

	freq_2 = []
	data_2 = []
	for j in coluna_2:
		if j not in data_2:
			data_2.append(j)

	for k in data_2:
		freq_2.append(coluna_2.count(k))

	ask1 = input('Deseja exibir o primeiro histograma? [yes/no] ')
	while ask1 not in {'yes', 'no'}:
		ask1 = input('Essa não é uma resposta válida! Deseja exibir o primeiro histograma? [yes/no] ')

	if ask1 == 'yes':
		histrograma(data_0,freq_0,'Histrograma das idades','Idade','Frequência')
	else:
		pass

	ask2 = input('Deseja exibir o segundo histograma? [yes/no] ')
	while ask2 not in {'yes', 'no'}:
		ask2 = input('Essa não é uma resposta válida! Deseja exibir o segundo histograma? [yes/no] ')

	if ask2 == 'yes':
		histrograma(data_1,freq_1,'Histrograma das alturas','Altura','Frequência')
	else:
		pass

	ask3 = input('Deseja exibir o terceiro histograma? [yes/no] ')
	while ask3 not in {'yes', 'no'}:
		ask3 = input('Essa não é uma resposta válida! Deseja exibir o terceiro histograma? [yes/no] ')

	if ask3 == 'yes':
		histrograma(data_2,freq_2,'Histrograma das massas','Massa','Frequência')
	else:
		pass

arquivo = 'dados_alunos.txt'
dados_alunos_histrogramas(arquivo)

print('\n----------------')
print('Exercício 2')
print('----------------')

def diretorio():
	for dirname, dirnames, filenames in os.walk('.'):
		for subdirname in dirnames:
			print(os.path.join(dirname,subdirname))

		for filename in filenames:
			print(os.path.join(dirname,filename))

diretorio()

print('\n----------------')
print('Exercício 3')
print('----------------')

print('O número de linhas no arquivo,', arquivo, 'é', wc.linecount(arquivo))
print('Quando o módulo (aula13_wc) é importado __name__ == aula13_wc e por causa disso o if statement é avaliado como False e não é executado.')
print('Quando o script (aula13_wc) é executado __name__ == __main__ e por causa disso o if statement é avaliado como True e é executado.')