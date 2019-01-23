def ler_arquivos(arquivo):
	try:
		file = open(arquivo)
	except:
		print('\nO arquivo não pode ser lido.')
		print('Verifique se o nome do arquivo está correto e se ele está no diretório que o script está sendo executado.')
		exit()

	ask = input('\nO arquivo %s que você deseja ler possui cabeçalho? [yes/no] ' % arquivo)
	while ask not in {'yes', 'no'}:
		ask = input('Essa não é uma resposta válida! Responda "yes" ou "no".')

	data = {}
	lista_auxiliar = []
	linhas = file.readlines()

	for i in linhas:
		column = i.strip().split('\t')
		lista_auxiliar.append(column)

	if ask == 'yes':
		for i in lista_auxiliar[0]:
			data[i] = []

		for i in range(1,len(lista_auxiliar)):
			for j in range(len(lista_auxiliar[i])):
				data[ lista_auxiliar[0][j] ].append(eval(lista_auxiliar[i][j]))
	else:
		for i in range(len(column)):
			data[i] = []

		for i in range(len(column)):
			for j in range(len(lista_auxiliar)):
				data[i].append(eval(lista_auxiliar[j][i]))

	return data, ask

if __name__ == '__main__':
	filename = input('Digite o nome do arquivo de texto que você deseja ler sem a extensão .txt: ')
	ler_arquivos(filename + '.txt')