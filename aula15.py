print('\n----------')
print('Aula 15')
print('----------')

import moduloT as T

print('\n----------------')
print('Exercício')
print('----------------')

print('O módulo moduloT foi feito no script moduloT.py.\n')

filename = input('Digite o nome do arquivo de texto que você deseja ler sem a extensão .txt: ')
arquivo = open(filename + '.txt')

linhas = arquivo.readlines()
arquivo.close()

data = []
for i in linhas:
    dados = i.split()
    fdados = [float(x) for x in dados]
    data.append(fdados)

dataT = T.transpor(data)

print('\nData =', data)
print('\nData transposta =', dataT)