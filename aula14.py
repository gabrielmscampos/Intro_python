print('\n----------')
print('Aula 14')
print('----------')

import ler_arquivos as ler
import matplotlib.pyplot as plt
import statistics

print('\n----------------')
print('Exercício 1 e 2')
print('----------------')

print('Foram feitos no arquivo ler_arquivos.py')

print('\n----------------')
print('Exercício 3 e 4')
print('----------------')

def histograma(data,freq,title,x_label,y_label):
	plt.bar(data,freq)
	plt.suptitle(title, fontsize = 14)
	plt.xlabel(x_label, fontsize = 12)
	plt.ylabel(y_label, fontsize = 12)
	plt.show()

def estatisticas(lista):
	media = statistics.mean(lista)
	dpp = statistics.pstdev(lista)
	dpa = statistics.stdev(lista)
	return media, dpp, dpa

filename = input('Digite o nome do arquivo de texto que você deseja ler sem a extensão .txt: ')
data, ask = ler.ler_arquivos(filename + '.txt')

valores = list(data.values())
chaves = list(data.keys())

frequencias = [[] for i in range(len(data))]
classes = [[] for i in range(len(data))]

medias = []
dpps = []
dpas = []

if ask == 'yes':
	for i in range(len(data)):
		for j in list(set(valores[i])):
			classes[i].append(j)

	for i in range(len(data)):
		for j in classes[i]:
			frequencias[i].append(valores[i].count(j))

	for i in range(len(data)):
		media, dpp, dpa = estatisticas(valores[i])
		medias.append(media)
		dpps.append(dpp)
		dpas.append(dpa)

	for i in range(len(data)):
		print('\nmean_',chaves[i] ,'=' , medias[i])
		print('pstdev_',chaves[i] ,'=' , dpps[i])
		print('stdev_',chaves[i] ,'=' , dpas[i])
		histograma(classes[i],frequencias[i],'Histograma da coluna {0}'.format(i),chaves[i],'Frequência')

else:
	for i in range(len(data)):
		for j in list(set(valores[i])):
			classes[i].append(j)

	for i in range(len(data)):
		for j in classes[i]:
			frequencias[i].append(valores[i].count(j))

	for i in range(len(data)):
		media, dpp, dpa = estatisticas(valores[i])
		medias.append(media)
		dpps.append(dpp)
		dpas.append(dpa)

	for i in range(len(data)):
		print('\nMédia da classe',i ,'=' , medias[i])
		print('Desvio padrão populacional da classe',i ,'=' , dpps[i])
		print('Desvio padrão amostral da classe',i ,'=' , dpas[i])
		histograma(classes[i],frequencias[i],'Histograma da coluna {0}'.format(i, i),'Classe da coluna {1}'.format(i, i),'Frequência')