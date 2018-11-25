"""

#---------------------------------------------------------------------------
# Projeto 1 - Pêndulo de Mola e pêndulo simples
# Alunos: Gabriel Moreira e Victor Augustus
# Professoras: Helena Malbouisson e Clemencia Mora
# Disciplina: Introdução a Python - UERJ 2018.2
#---------------------------------------------------------------------------

Esse programa tem como objetivo reproduzir o movimento de um pêndulo de mola, ou seja, como se comporta a posição do objeto anexado a uma bolaa mercer da força gravitacional.
Além disso, o programa oferece a opção de reproduzir o movimento do pêndulo simples, com as mesmas condições inicias do pêndulo de mola, para fins de comparação.
Inicialmente o usuário deve fornecer as coordenadas cartesianas da posição inicial do objeto, em condições normais a coordenada x pode ser positiva ou negativa e a coordenada z deve ser negativa, assim o programa converte as coordenadas para o sistema polar e calcula as acelerações a cada instante com de 0,0001 segundos com os dados da coordenada radial e angular.
Então, o programa calcula as velocidades e posições, a cada instante, através de uma de Riemann.
Após coletar e calcular todos os dados, o programa armazena em um arquivo .txt e plota os gráficos relativos ao movimento.
"""

from math import *
import matplotlib.pyplot as plt

def pendulo_mola():
	# Propriedades do Pêndulo
	g = 9.81                                                                                  # valor padrão para aceleração gravitacional (m/s²)
	l0 = float(input('\nDigite o comprimento natural da mola em (m): '))                      # comprimento natural da mola (m)
	k = float(input('Digite a constante elástica da mola em (N/m): '))                        # constante elástica da mola (kg/s²)
	m = float(input('Digite a massa do objeto acoplado a mola em (kg): '))                    # massa do objeto acoplado a mola (kg)

	# Condições iniciais
	ivy = int(input('\nVocê deseja inserir as condições em iniciais em coordenadas polares ou cartesianas? [Polares == 0, Cartesianas =/ 0]: '))       # pergunta ao usuário como ele deseja inserir as condições iniciais
	if ivy == 0:
		r = float(input('\nDigite a posição radial do objeto em (m): '))                                    # input do usuário da distância radial inicial em (m)
		theta = radians(float(input('Digite o ângulo inicial com a vertical do objeto em (graus): ')))      # input do usuário do ângulo inicial em graus que é logo convertido para radianos com a função radians()
		x = r*sin(theta)                                                                                    # passa o input polar para a coordenada cartesiana x
		z = -r*cos(theta)                                                                                   # passa o input polar para a coordenada cartesiana z
		vx = 0                                                                                    # velocidade inicial na direção x (m/s)
		vz = 0                                                                                    # velocidade inicial em z (m/s/
	else:
		x = float(input('\nDigite a posição inicial no eixo x do objeto em (m): '))               # posição inicial do objeto no eixo x (m)
		z = float(input('Digite a posição inicial no eixo -z do objeto em (m): '))                # posição inicial do objeto no eixo z (m)
		vx = 0                                                                                    # velocidade inicial na direção x (m/s)
		vz = 0                                                                                    # velocidade inicial em z (m/s)

	# Definindo o tempo inicial, o tempo de movimento e o time-step da integração
	t = 0                                                                                     # tempo inicial (s)
	tf = float(input('\nDigite o tempo em (s) transcorrido no movimento: '))                         # tempo final (s)
	dt = 0.0001                                                                               # time-step (S)

	# Cálculo das coordenadas polares
	def calcular_r(x,z):                            # função que calcula a distâcia radial inicial em (m)
		r = sqrt(x**2 + z**2)                       # distância radial em (m)
		return r                                    # returna r na função

	def calcular_theta(x,z):                        # função que calcula o ângulo inicial em (rad)
		theta = 0                                   # a função atan2(x,z) é uma generalização da função atan(x,z)
		if (z<0):
			theta = atan(-x/z)
		elif (x>0 and z>=0):
			theta = pi/2 + atan(z/x)
		elif (x<0 and z>=0):
			theta = -pi/2 + atan(z/x)
		elif (x==0):
			theta = 0
		return theta                                # retorna theta na função

	# Cálculo das acelerações com relação as coordenadas polares
	def calcular_acelerações(r,theta):              # função que calcula todas as acelerações
		ax = -(k/m)*(r-l0)*sin(theta)               # aceleração em x
		az = (k/m)*(r-l0)*cos(theta) - g            # aceleração em z
		a = sqrt(ax**2 + az**2)                     # módulo da aceleração
		return ax, az, a                            # retorna ax, az, a na função

	def calcular_velocidades(vx,vz,ax,az):          # função que calcula todas as velocidades
		vx = vx + ax*dt                             # velocidade em x
		vz = vz + az*dt                             # velocidade em z
		v = sqrt(vx**2 + vz**2)                     # módulo da velocidade
		return vx, vz, v                            # retorna vx, vz, v na função

	def calcular_posições(x,z,vx,vz):               # função que calcula as posições no sistema cartesiano
		x = x + vx*dt                               # posição x (m)
		z = z + vz*dt                               # posição z (m)
		return x, z                                 # retorna x e z na função

	# Cálculo da energia do sistema
	def calcular_energia(r,z,v):
		cinética = (1/2)*m*v**2                                   # energia cinética
		potencial_grav = m*g*(l0-z)                               # energia potencial gravitacional
		portencial_elast = (1/2)*k*(l0-r)**2                      # energia potencial elástica
		energia = cinética + potencial_grav + portencial_elast    # energia mecânica
		return energia                                            # retorna a energia na função

	# # Criando as listas vazias e função de append
	t_list = []                            # lista para os valores de tempo
	x_list = []                            # lista para os valores de x
	z_list = []                            # lista para os valores de z
	vx_list = []                           # lista para os valores de vx
	vz_list = []                           # lista para os valores de vz
	v_list = []                            # lista para os valores de v
	ax_list = []                           # lista para os valores de ax
	az_list = []                           # lista para os valores de az
	a_list = []                            # lista para os valores de a
	r_list = []                            # lista para os valores de r
	energia_list = []                      # lista para os valores da energia total do sistema

	def append_func():                     # função para acrescentar as lista as variáveis
		t_list.append(t)                   # acrescenta a lista t_list o valor de t
		x_list.append(x)                   # acrescenta a lista x_list o valor de t
		z_list.append(z)                   # acrescenta a lista z_list o valor de t
		vx_list.append(vx)                 # acrescenta a lista vx_list o valor de t
		vz_list.append(vz)                 # acrescenta a lista vz_list o valor de t
		v_list.append(v)                   # acrescenta a lista v_list o valor v
		ax_list.append(ax)                 # acrescenta a lista ax_list o valor de ax
		az_list.append(az)                 # acrescenta a lista az_list o valor de az
		a_list.append(a)                   # acrescenta a lista a_list o valor de a
		r_list.append(r)                   # acrescenta a lista r_list o valor de r
		energia_list.append(energia)       # acrescenta a lista energia_lista o valor de energia

	# Atualizando os valores do movimento
	while (t <= tf):
		r = calcular_r(x,z)                                         # atualiza o valor de r
		theta = calcular_theta(x,z)                                 # atualiza o valor de theta
		ax, az, a = calcular_acelerações(r,theta)                   # atualiza o valor de (ax, az, a)
		vx, vz, v = calcular_velocidades(vx,vz,ax,az)               # atualiza o valor de (vx,vz,v)
		x, z = calcular_posições(x,z,vx,vz)                         # atualiza o valor de (x,z)
		energia = calcular_energia(r,z,v)                           # atualiza o valor da energia total
		t = t + dt                                                  # atualiza o valor de t

		append_func()                                               # chama a função append_func()

	# Criando um arquivo .txt e armazenando os dados calculados
	arq1 = open('dados_pendulo_de_mola.txt', 'w')
	arq1.write('t(s)       x(m)       z(m)        vx(m/s)     vz(m/s)     ax(m/s²)     az(m/s²)     energia(J)' )
	arq1.write('\n')
	for index in range(0,len(t_list)):                              # faz um loop que escreve os dados com relação ao tamanho da lista t_list de referência
		arq1.write(str("%.4f" % t_list[index]))                     # escreve o dados em t_list
		arq1.write('     ')
		arq1.write(str("%.4f" % x_list[index]))                     # escreve o dados em x_list
		arq1.write('     ')
		arq1.write(str("%.4f" % z_list[index]))                     # escreve o dados em z_list
		arq1.write('     ')
		arq1.write(str("%.4f" % vx_list[index]))                    # escreve o dados em vx_list
		arq1.write('     ')	
		arq1.write(str("%.4f" % vz_list[index]))                    # escreve o dados em vz_list
		arq1.write('     ')	
		arq1.write(str("%.4f" % ax_list[index]))                    # escreve o dados em ax_list
		arq1.write('     ')	
		arq1.write(str("%.4f" % az_list[index]))                    # escreve o dados em az_list
		arq1.write('     ')	
		arq1.write(str("%.4f" % energia_list[index]))               # escreve o dados em energia_list
		arq1.write('\n')			
	arq1.close()

	# Graficando
	def plot_movimento1(tamanho,x,f,x_label,y_label):                         # função que faz o plotting com o gráfico em format T
		fig1 = plt.figure()
		ax1 = fig1.add_subplot(1,1,1)
		ax1.spines['left'].set_position('center')                             # movimenta o eixo na esquerda para o centro
		ax1.spines['bottom'].set_position('zero')                             # movimenta o eixo de baixo para o 0
		ax1.spines['right'].set_color('none')                                 # apaga o eixo na direita
		ax1.spines['top'].set_color('none')                                   # apaga o eixo superior
		ax1.set_xlabel(x_label)                                               # da nome ao eixo inferior
		ax1.set_ylabel(y_label)                                               # da nome ao eixo da esquerda

		plt.plot(x,f)                                                         # plot (x,f(x))
		plt.axis([(-tamanho-0.25), (tamanho+0.25), (-tamanho-0.25), 1])       # define o tamanho dos eixos (x,y)
		plt.show()                                                            # mostra o gráfico na tela
		plt.close()

	def plot_gráfico(x,f,x_label,f_label):                                    # função que faz o plotting com o gráfico convencional
		plt.plot(x,f)                                                         # plot (x,f(x))
		plt.xlabel(x_label)                                                   # da nome ao eixo inferior
		plt.ylabel(f_label)                                                   # da nome ao eixo superior
		plt.show()                                                            # mostrar o gráfico na tela
		plt.close()

	plot_movimento1(max(r_list),x_list,z_list,'Posição x (m)','Posição z (m)')          # plotting em formato T de (x,z)
	plot_gráfico(x_list,z_list,'Posição x (m)','Posição z (m)')                         # plotting de (x,z)
	plot_gráfico(t_list,v_list,'Tempo (s)','Velocidade (m/s)')                          # plotting de (t,v)
	plot_gráfico(t_list,r_list,'Tempo (s)','Posição radial (m)')                        # plotting de (t,r)
	plot_gráfico(t_list,a_list,'Tempo (s)','Aceleração (m/s²)')                         # plotting de (t,a)
	plot_gráfico(x_list,vx_list,'Posição x (m/s)','Velocidade x (m/s)')                 # plotting de (x,vx)
	plot_gráfico(z_list,vz_list,'Posição z (m/s)','Velocidade z (m/s)')                 # plotting de (z,vz)
	plot_gráfico(vx_list,vz_list,'Velocidade x (m/s)','Velocidade z (m/s)')             # plotting de (vx,vz)

	def pendulo_simples(g,tf,dt,x_list,z_list):                               # função para o cálculo do movimento de um pêndulo simples
		# Propriedades do Pêndulo
		u1 = float(x_list[0])                                                 # variável u1 que retoma o valor inicial escolhido pelo usuário para x
		u2 = float(z_list[0])                                                 # variável u2 que retoma o valor inicial escolhido pelo usuário para z
		l = sqrt(u1**2 + u2**2)                                               # comprimento do fio em coordenadas polares a partir de (x,z)

		# Condições iniciais
		theta = calcular_theta(u1,u2)                                         # cálcula o ângulo inicial (rad) a partir de (x,z) com a função calcular_theta(x,z)
		vx = 0                                                                # velocidade inicial na direção x (m/s)
		vz = 0                                                                # velocidade inicial em z (m/s)
		w = 0                                                                 # velocidade angular inicial em (rad/s)
		t = 0                                                                 # tempo inicial (s)

		# Cálculo das posições:
		def posi_cartesiana(theta):                                           # função que calcula a posição em coordenadas cartesianas (x,z) em (m)
			x = l*sin(theta)                                                  # posição x (m)
			z = -l*cos(theta)                                                 # posição z (m)
			return x, z                                                       # retorna o valor de (x,z) na função

		# Cálculo das velocidades
		def calcular_velocidades(w,theta):                                    # função que calcula as velocidades (vx,vz,v) em (m/s)
			vx = l*w*cos(theta)                                               # velocidade no eixo x (m/s)
			vz = l*w*sin(theta)                                               # velocidade no eixo z (m/s)
			v = sqrt(vx**2 + vz**2)                                           # módulo da velocidade (m/s)
			return vx, vz, v                                                  # retorna (vx,vz,v) na função

		# Cálculo das acelerações
		def calcular_acelerações(w,theta):                                    # função que calcula as acelerações (ax,az,a) em (m/s²)
			ax = -g*cos(theta)*sin(theta) - l*(w**2)*sin(theta)               # aceleração no eixo x em (m/s²)
			az = -g*(sin(theta)**2) + l*(w**2)*cos(theta)                     # aceleração no eixo z em (m/s²)
			a = sqrt(ax**2 + az**2)                                           # módulo da aceleração em (m/s²)
			return ax, az, a                                                  # retorna (ax,az,a) na função

		#Cálculo das grandezas polares
		def calcular_polares(w,theta,dt):                                     # função que calcula as grandezas em coordenadas polares
			alfa = -(g/l)*sin(theta)                                          # aceleração angular em (rad/s²)
			w = w + alfa*dt                                                   # velocidade angular em (rad/s)
			theta = theta + w*dt                                              # ângulo com o eixo -z (graus)
			return alfa, w, theta                                             # retorna o valor de (alfa,w,theta) na função

		def calcular_energia(r,z,v):                                          # função que calcula a energia mecânica em (J)
			cinética = (1/2)*m*v**2                                           # energia cinética (J)
			potencial_grav = m*g*(-z)                                         # energia potencial gravitacional (J)
			energia = cinética + potencial_grav                               # energia mecânica (J)
			return energia                                                    # retorna a energia na função

		# Criando as listas vazias e função de append
		t_simples_list = []                                                   # lista para os valores de tempo
		x_simples_list = []                                                   # lista para os valores de x
		z_simples_list = []                                                   # lista para os valores de z
		vx_simples_list = []                                                  # lista para os valores de vx
		vz_simples_list = []                                                  # lista para os valores de vz
		v_simples_list = []                                                   # lista para os valores de v
		ax_simples_list = []                                                  # lista para os valores de ax
		az_simples_list = []                                                  # lista para os valores de az
		a_simples_list = []                                                   # lista para os valores de a
		energia_simples_list = []                                             # lista para os valores da energia total do sistema

		def append_simples_func():                                            # função para acrescentar as lista as variáveis
			t_simples_list.append(t)                                          # acrescenta a lista t_simples_list o valor de t
			vx_simples_list.append(vx)                                        # acrescenta a lista x_simples_list o valor de x
			vz_simples_list.append(vz)                                        # acrescenta a lista z_simples_list o valor de z
			x_simples_list.append(x)                                          # acrescenta a lista vx_simples_list o valor de vx
			z_simples_list.append(z)                                          # acrescenta a lista vz_simples_list o valor de vz
			v_simples_list.append(v)                                          # acrescenta a lista v_simples_list o valor de v
			ax_simples_list.append(ax)                                        # acrescenta a lista ax_simples_list o valor de ax
			az_simples_list.append(az)                                        # acrescenta a lista az_simples_list o valor de az
			a_simples_list.append(a)                                          # acrescenta a lista a_simples_list o valor de a
			energia_simples_list.append(energia)                              # acrescenta a lista energia_simples_list o valor de energia

		# Atualizando os valores do movimento
		while(t <= tf):
			x, z = posi_cartesiana(theta)                                     # atualiza os valores de (x,z)
			vx, vz, v = calcular_velocidades(w,theta)                         # atualiza os valores de (vx,vz,v)
			ax, az, a = calcular_acelerações(w,theta)                         # atualiza os valores de (ax,az,a)
			alfa, w, theta = calcular_polares(w,theta,dt)                     # atualiza os valores de (alfa,w,theta)
			energia = calcular_energia(r,z,v)                                 # atualiza os valores de energia
			t = t + dt                                                        # atualiza os valores de t

			append_simples_func()                                             # chama a função append_simples_func()

		arq2 = open('dados_pendulo_simples.txt', 'w')
		arq2.write('t(s)       x(m)       z(m)        vx(m/s)     vz(m/s)     ax(m/s²)     az(m/s²)     energia(J)' )
		arq2.write('\n')
		for index in range(0,len(t_simples_list)):                            # faz um loop que escreve os dados com relação ao tamanho da lista t_simples_list de referência
			arq2.write(str("%.4f" % t_simples_list[index]))                   # escreve o dados em t_simples_list
			arq2.write('     ')
			arq2.write(str("%.4f" % x_simples_list[index]))                   # escreve o dados em x_simples_list
			arq2.write('     ')
			arq2.write(str("%.4f" % z_simples_list[index]))                   # escreve o dados em z_simples_list
			arq2.write('     ')
			arq2.write(str("%.4f" % vx_simples_list[index]))                  # escreve o dados em vx_simples_list
			arq2.write('     ')	
			arq2.write(str("%.4f" % vz_simples_list[index]))                  # escreve o dados em vz_simples_list
			arq2.write('     ')	
			arq2.write(str("%.4f" % ax_simples_list[index]))                  # escreve o dados em ax_simples_list
			arq2.write('     ')	
			arq2.write(str("%.4f" % az_simples_list[index]))                  # escreve o dados em az_simples_list
			arq2.write('     ')	
			arq2.write(str("%.4f" % energia_simples_list[index]))             # escreve o dados em energia_simples_list
			arq2.write('\n')			
		arq2.close()

		def plot_movimento2(tamanho,x,f,x_label,y_label):                     # função que faz o plotting com o gráfico em format T
			fig2 = plt.figure()
			ax2 = fig2.add_subplot(1,1,1)
			ax2.spines['left'].set_position('center')                         # movimenta o eixo na esquerda para o centro
			ax2.spines['bottom'].set_position('zero')                         # movimenta o eixo de baixo para o 0
			ax2.spines['right'].set_color('none')                             # apaga o eixo na direita
			ax2.spines['top'].set_color('none')                               # apaga o eixo superior
			ax2.set_xlabel(x_label)                                           # da nome ao eixo inferior
			ax2.set_ylabel(y_label)                                           # da nome ao eixo da esquerda

			plt.plot(x,f)                                                     # plot (x,f(x))
			plt.axis([(-tamanho-0.25), (tamanho+0.25), (-tamanho-0.25), 1])   # define o tamanho dos eixos (x,y)
			plt.show()                                                        # mostra o gráfico na tela
			plt.close()

		plot_movimento2(l,x_simples_list,z_simples_list,'Posição x (m)','Posição z (m)')             # plotting em formato T de (x,z)
		plot_gráfico(x_simples_list,z_simples_list,'Posição x (m)','Posição z (m)')                  # plotting de (x,z)
		plot_gráfico(t_simples_list,v_simples_list,'Tempo (s)','Velocidade (m/s)')                   # plotting de (t,v)
		plot_gráfico(t_simples_list,a_simples_list,'Tempo (s)','Aceleração (m/s²)')                  # plotting de (t,a)
		plot_gráfico(x_simples_list,vx_simples_list,'Posição x (m/s)','Velocidade x (m/s)')          # plotting de (x,vx)
		plot_gráfico(z_simples_list,vz_simples_list,'Posição z (m/s)','Velocidade z (m/s)')          # plotting de (z,vz)
		plot_gráfico(vx_simples_list,vz_simples_list,'Velocidade x (m/s)','Velocidade z (m/s)')      # plotting de (vx,vz)

	pergunta = int(input('\nVocê deseja executar a função do pêndulo simples? [True == 0]: '))       # pergunta se o usuário deseja executar a função do pêndulo_simples
	if pergunta == 0:                                                                                # avalia se a pergunta foi sim ou não (lógica booleana)
		pendulo_simples(g,tf,dt,x_list,z_list)                                                       # executa a função do pendulo_simples
		print('\nEncerrando o programa!\n')                                                          # pinta na tela que o programa foi encerrado após a execução da função
	else:                                                                                            # caso a resposta seja /= 0
		print('\nEncerrando o programa!\n')                                                          # printa na tela que o programa foi encerrado

pendulo_mola()