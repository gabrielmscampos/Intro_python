"""
#---------------------------------------------------------------------------
# Projeto 2 - Cinemática de colisões relativísticas (Aniquilação elétron-pósitron)
# Aluno: Gabriel Moreira e Victor Augustus
# Professoras: Helena Malbouisson e Clemencia Mora
# Disciplina: Introdução a Python - UERJ 2018.2
#---------------------------------------------------------------------------

Script desenvolvido para simulações de colisões relativísticas com foco em aniquilação elétron-pósitron.
Com a colisão de um pósitron de momentum randômico com um elétron em repouso no referencial do laboratório foi possível calcular a energia final dos fótons resultandos
	pelo princípio de conservação de energia com base em um distribuição de ângulos finais de um dos fótons.

Source: https://arxiv.org/pdf/1011.1943.pdf

Obs:
O script tem dependências com os packages numpy, pandas e openpyxl.
Caso o script não funcione executando no terminal com --python3 projeto2.py é preciso instalar esses packages pelo terminal da seguinte maneira:

sudo apt install python3-pip
pip3 install pandas
pip3 install openpyxl
"""

# Módulos utilizados
from math 					import *
from particula 				import *
from random 				import *
import matplotlib.pyplot	as plt
import numpy 				as np
import pandas 				as pd
from pandas 				import ExcelWriter

# Definindo as funções
def aniquilacao_ep(Ep,Ee,theta):
	k = sqrt((Ep - Ee)/(Ep + Ee))
	Ef = Ee/(1-k*cos(radians(theta)))
	return Ef

def plot(dict,x_label,y_label,title):
	for i in range(1,n_colisoes+1):
		data_x = np.array(dict['Colisão ' + str(i)][0])
		data_y = np.array(dict['Colisão ' + str(i)][1])
		plt.plot(data_x,data_y, label = 'Colisão ' + str(i))
		plt.xlabel(x_label, fontsize = 12)
		plt.ylabel(y_label + '1 (MeV)', fontsize = 12)

	plt.title(title, fontsize = 14)
	plt.legend(bbox_to_anchor = (1.04,1), loc = 'upper left')
	plt.tight_layout(rect = [0,0,0.75,1])
	plt.savefig('foton1.png')
	plt.show()
	plt.close()

	for i in range(1,n_colisoes+1):
		data_x = np.array(dict['Colisão ' + str(i)][0])
		data_y = np.array(dict['Colisão ' + str(i)][2])
		plt.plot(data_x,data_y, label = 'Colisão ' + str(i))
		plt.xlabel(x_label, fontsize = 12)
		plt.ylabel(y_label + '2 (MeV)', fontsize = 12)

	plt.title(title, fontsize = 14)
	plt.legend(bbox_to_anchor = (1.04,1), loc = "upper left")
	plt.tight_layout(rect = [0,0,0.75,1])
	plt.savefig('foton2.png')
	plt.show()
	plt.close()

# Apresentando o programa ao usuário e coletando o número de colisões
print('\nProjeto de Colisões Relativísticas, com foco em Aniquilação Elétron-Pósitron \n Foi utilizado um sistema de unidades naturais onde c = 1')
print('\bO programa irá calcular a energia final dos fótons resultantes da colisão de um elétron com momentum p = 0 e um pósitron com momentum p randômico entre 1.0 e 100.0.')
print('No final do processo, iniciará a plotagem dos gráficos da distribuição do ângulo resultante do fóton 1 pela distribuição da energa final dos fótons 1 e 2, além disso, o script também irá armazenar os dados.')
n_colisoes = int(input('\nDigite o número de colisões: '))
while n_colisoes <= 0:
	n_colisoes = int(input('Essa resposta não é válida! Digite um número > 0: '))

# Definindo o dicionário que irá armazenar os dados
dist = {}

for i in range(1,n_colisoes+1):
	dist['Colisão ' + str(i)] = [[] for i in range(6)]

# Criando um loop com a variável loop_question para reiniciar o programa depedendo da resposta do usuário
loop_question = 'sim'
while loop_question == 'sim':

	# Loop
	for i in range(1,n_colisoes+1):
		p = uniform(1.0,100.0)
		e = Particula(0.511)
		pos = Particula(0.511,p)

		theta = 0
		while theta <= 360:
			Ef = aniquilacao_ep(pos.energia(),e.energia(),theta)
			fot1 = Particula(0,Ef)
			fot2 = Particula(0,(pos.energia()+e.energia())-Ef)

			dist['Colisão ' + str(i)][0].append(theta)
			dist['Colisão ' + str(i)][1].append(fot1.energia())
			dist['Colisão ' + str(i)][2].append(fot2.energia())
			dist['Colisão ' + str(i)][3].append(e.energia())
			dist['Colisão ' + str(i)][4].append(pos.energia())
			dist['Colisão ' + str(i)][5].append(p)

			theta += 1

	# Gráfico
	plot(dist,'\u03B8 (\u00B0)', 'Energia \u03B3_', 'Aniquilação Elétron-Pósitron')

	# Criando um arquivo .txt e armazenando os dados calculados
	arq = open('dados_aniquilação_ep.txt', 'w')
	for i in range(1,n_colisoes+1):
		arq.write('\n############### Colisão ' + str(i) + ' ###############')
		arq.write('\np_pos(MeV/c)		\u03B8 (\u00B0)		E_e(MeV)		E_pos(MeV)		E_e+p(MeV)		E_\u03B3_1(MeV)		E_\u03B3_2(MeV)		E_\u03B3_1+\u03B3_2(MeV)')
		arq.write('\n')
		for j in range(0,len(dist['Colisão 1'][0])):
			arq.write(str("%.4f" % dist['Colisão ' + str(i)][5][j]))
			arq.write('			')
			arq.write(str("%.4f" % dist['Colisão ' + str(i)][0][j]))
			arq.write('			')
			arq.write(str("%.4f" % dist['Colisão ' + str(i)][3][j]))
			arq.write('			')
			arq.write(str("%.4f" % dist['Colisão ' + str(i)][4][j]))
			arq.write('			')
			arq.write(str("%.4f" % (dist['Colisão ' + str(i)][3][j] + dist['Colisão ' + str(i)][4][j])))
			arq.write('			')
			arq.write(str("%.4f" % dist['Colisão ' + str(i)][1][j]))
			arq.write('			')	
			arq.write(str("%.4f" % dist['Colisão ' + str(i)][2][j]))
			arq.write('			')	
			arq.write(str("%.4f" % (dist['Colisão ' + str(i)][1][j] + dist['Colisão ' + str(i)][2][j])))
			arq.write('\n')			
	arq.close()

	# Criando um arquivo .xlsx e armazenando os dados cada sheet do excel
	writer = ExcelWriter("dados_aniquilação_ep.xlsx")

	Df_List = []

	for i in range(1, n_colisoes + 1):

		theta 		= np.array(dist['Colisão ' + str(i)][0])
		E_fot1_ene	= np.array(dist['Colisão ' + str(i)][1])
		E_fot2_ene 	= np.array(dist['Colisão ' + str(i)][2])
		E_ene		= np.array(dist['Colisão ' + str(i)][3])
		P_ene		= np.array(dist['Colisão ' + str(i)][4])
		P			= np.array(dist['Colisão ' + str(i)][5])

		My_data_frame = pd.DataFrame({ "p_pos(MeV/c)": P,
										"\u03B8 (\u00B0)": theta,
										"E_e(MeV)": E_ene,
										"E_pos(MeV)": P_ene,
										"E_e+p(MeV)": E_ene + P_ene,
										"E_\u03B3_1(MeV)": E_fot1_ene,
										"E_\u03B3_2(MeV)": E_fot2_ene,
										"E_\u03B3_1+\u03B3_2(MeV)": E_fot1_ene + E_fot2_ene
									})

		Df_List.append(My_data_frame)

	for i in range(len(Df_List)):
		#print (Df_List)
		col_string = 'Sheet_' + str(i+1)
		Df_List[i].to_excel(writer, col_string, index=False)
		writer.save()

	# Update da loop_question para saber se o usuário quer realizar outras simulações
	loop_question = input('\nDeseja simular outras colisões? [sim/não] ')
	while loop_question not in {'sim', 'não'}:
		loop_question = input('Essa não é uma resposta válida! Responda [sim] ou [não]. ')

	# Atualizando a condição inicial do número de colisões para o caso que o usuário deseja realizar outras simulações
	if loop_question == 'sim':
		n_colisoes = int(input('Digite o número de colisões: '))
		while n_colisoes <= 0:
			n_colisoes = int(input('Essa resposta não é válida! Digite um número > 0: '))

	# Limpando o dicionário que irá armazenar os dados para o caso que o usuário deseja realizar outras simulações
		dist = {}

		for i in range(1,n_colisoes+1):
			dist['Colisão ' + str(i)] = [[] for i in range(6)]

print('\nEncerrando o programa!')