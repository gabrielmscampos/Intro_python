print('------------------')
print('Aula 3')
print('------------------')

import math

print('\nExercício 1\n')

def valortipo(argumento):
	print('O valor do argumento é:', argumento) #Imprime o valor do argumento
	print('O argumento é do tipo:', type(argumento)) #Imprime o tipo do argumento

argumento = 'Hello World' #Define qual é o argumento
valortipo(argumento) #Chama a função valortipo

print('\nExercício 2\n')

def velocidade_mru(x,x_0,t):
	v = (x-x_0)/t #Calcula a velocidade média no MRU
	print('A velocidade média é', v, 'm/s\n') #Imprime a velocidade média

x = eval(input('Qual a posição final do objeto em metros? ')) #Pergunta e armazena a informação da posição final do objeto
x_0 = eval(input('Qual a posição inicial do objeto em metros? ')) #Pergunta e armazena a informação da posição incial do objeto
t = eval(input('Quantos segundos foram transcorridos durante o movimento? ')) #Pergunta e armazena a informãção o tempo transcorrido
velocidade_mru(x,x_0,t) #Chama a função velocidade_mru

def velocidade_mruv(g,t): #Calcula e imprime a velocidade de queda de um objeto solto com velocidade incial 0
	v = g*t
	print('A velocidade de queda do objeto é', v, 'm/s')

g = 9.8 #Constante de aceleração gravitacional
t = eval(input('Quantos segundos foram transcorridos durante a queda? ')) #Pergunta e armazena o tempo transcorrido da queda
velocidade_mruv(g,t) #Chama a função velocidade_mruv

print('\nExercício 3\n')

def angzenital(h,d): #Calcula e imprime o ângulo zenital com aproximação para pequenos ângulos (tan(theta) = theta )
	theta = d/h
	print('O ângulo zenital do sol é:', theta, 'radianos')

d = eval(input('Qual o tamanho da sombra feita pelo poste em metros? ')) #Pergunta e armazena o tamanho da sombra
h = eval(input('Qual a altura do poste em metros? ')) #Pergunta e armazena a altura do poste
angzenital(h,d) #Chama a função angzenital

print('\nExercício 4\n')

def m_to_mi(m): #Converte metros para milhas
	mi = m/1609.344
	return mi

def mi_to_m(mi): #Converte milhas para metros
	m = mi*1609.344
	return m

def m_to_km(m): #Converte metros para kilometros
	km = m*10**(-3)
	return km

def min_to_h(minutos): #Converte minutos para horas
	h = minutos/60
	return h

def h_to_s(h): #Converte horas para segundos
	s = h*3600
	return s

def s_to_h(s): #Converte segundos para horas
	h = s/3600
	return h

def v_m(d,t): #Calcula e imprime a velocidade média
	v_m = m_to_km(mi_to_m(d))/min_to_h(t)
	print('\nA velocidade média é', v_m, 'km/h')

def t_m(t,d): #Calcula e imprime o tempo médio
	t_m = h_to_s(min_to_h(t))/m_to_km(mi_to_m(d))
	print('O tempo médio é', t_m, 's/km')

t = eval(input('A corrida durou quantos minutos? ')) #Pergunta e armazena o tempo em minutos do movimento
d = eval(input('Quantas milhas foram percorridas? ')) #Pergunta e armazena a distância percorrida em milhas
v_m(d,t) #Chama a função v_m
t_m(t,d) #Chama a função t_m

print('\nExercício 5\n')

def imc(m,h): #Calcula e imprime o imc com base na massa em kilogramas e a altura em metros
	imc = m/(h**2)
	print('O seu IMC é', imc, '\n')

m = eval(input('Quantos kilogramas você pesa? ')) #Pergunta e armazena a massa
h = eval(input('Quantos metros de altura você tem? ')) #Pergunta e armazena a altura
imc(m,h) #chama a função imc

def vesf(r): #Calcula e imprime o volume de um esfera de raio r
	v = (4*math.pi*(r**3))/3
	print('O volume da esfera é', v, 'm³\n')

r = eval(input('Quantos metros tem o raio da esfera? ')) #Pergunta e armazena o raio da esfera
vesf(r) #Chama a função vesf

def m_to_mm(m): #Converte metros em milimetros
	mm = m*(10**(3))
	return mm

def nm_to_mm(nm): #Converte nanometros em milimetros
	mm = nm*(10**(-6))
	return mm

def distmax(lmb,D,d): #Calcula e imprime a distância maxima entre dois máximos de interferência consecutivos com base
	dy = (nm_to_mm(lmb)*m_to_mm(D))/d
	print('A distância máxima entre dois máximos de interferênia consecutivos é', dy, 'mm\n')

lmb = eval(input('Qual o comprimento de onda (em nanometros) do laser? ')) #Pergunta e armazena o comprimento de onda
D = eval(input('Qual a distância (em metros) do anteparo até a fenda? ')) #Pergunta e armazena a distância do anteparo até a fenda
d = eval(input('Qual o tamanho (em milimetros) da fenda? ')) #Pergunta e armazena o tamanho da fenda
distmax(lmb,D,d) #chama a função distmax