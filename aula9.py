print('----------------')
print('Aula 9')
print('----------------')

from math import *
import matplotlib.pyplot as plt

print('\n----------------')
print('Exercício 1')
print('----------------')

# Condições iniciais
d = 0                           # distância inicial
d_max = 5                       # distância máxima em (km)
v1 = 12                         # velocidade suficientemente constante em (km/h)
t = 0                           # tempo inicial
dt = 1                          # time-step em (min)

def h_to_min(v_h):              # função que transforma a velocidade de km/h para km/min
	v_min = v_h/60
	return v_min

v1 = h_to_min(v1)

tempo = []
dist_percorrrida = []

while d != d_max:
	tempo.append(t)
	d = v1*t
	t = t + dt
	dist_percorrrida.append(d)

print('\nLista com o intervalo de tempo de 1 minuto:', tempo)
print('\nLista com a distância percorrida no intervalo de tempo:', dist_percorrrida)

print('\n----------------')
print('Exercício 2')
print('----------------')

#FALTA ESSE EXERCÍCIO

print('\n----------------')
print('Exercício 3')
print('----------------')

# Propriedades do pêndulo
l = 1                                             # comprimento do fio em (m)
m = 0.2                                           # massa do objeto em (kg)
g = 9.8                                           # aceleração gravitacional em (m/s²)

# Condições iniciais
theta = radians(30)                               # ângulo inicial de 30 graus
vx = 0                                            # velocidade inicial na direção x (m/s)
vz = 0                                            # velocidade inicial em z (m/s)
w = 0                                             # velocidade angular inicial em (rad/s)
t = 0                                             # tempo inicial (s)
tf = 30                                           # tempo final (s)
dt = 0.0001                                       # time-step (s)

# Posições cartesianas iniciais
x = l*sin(theta)                                  # posição x (m)
z = -l*cos(theta)                                 # posição z (m)

# Criando as listas vazias
t_list = []                                       # lista para os valores de tempo
x_list = []                                       # lista para os valores de x
z_list = []                                       # lista para os valores de z

# Atualizando os valores do movimento
while t <= tf:
	x = l*sin(theta)                              # atualiza os valores de x (coordenada cartesiana x)
	z = -l*cos(theta)                             # atualiza os valores de z (coordenadas cartesiana z)
	alfa = -(g/l)*sin(theta)                      # atualiza os valores de alfa (aceleração angular)
	w = w + alfa*dt                               # atualiza os valores de w (velocidade angular)
	theta = theta + w*dt                          # atualiza os valores de theta (posição angular)
	t = t + dt                                    # atualiza os valores de t (tempo)

	t_list.append(t)                              # acrescenta a lista t_list o valor de t
	x_list.append(x)                              # acrescenta a lista x_list o valor de x
	z_list.append(z)                              # acrescenta a lista z_list o valor de z

def plot_gráfico(x,f,x_label,f_label):            # função que faz o plotting com o gráfico convencional
	plt.plot(x,f)                                 # plot (x,f(x))
	plt.xlabel(x_label)                           # da nome ao eixo inferior
	plt.ylabel(f_label)                           # da nome ao eixo superior
	plt.show()                                    # mostrar o gráfico na tela
	plt.close()

print('Gráfico da posição x (m) com relação a z (m) do pêndulo simples.')
plot_gráfico(x_list,z_list,'Posição x (m)','Posição z (m)')                         # plotting de (x,z)