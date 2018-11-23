#Exercício 1

d_percorrido=10/1.61
t=43.5/60
t_med=t/d_percorrido
v_med=d_percorrido/t

print('O tempo médio por milha é,', t_med, 'h/mi.')
print('A velocidade média é,', v_med, 'mi/h')

#Exercício 2

v_som=343
v_luz=3*(10**8)
t=3
d=v_som*t

print('A distância é,', d, 'metros')

#Exercício 3

a=3
b=-4
c=-10
delta=b**2-4*a*c
x_1=(-b-delta**0.5)/(2*a)
x_2=(-b+delta**0.5)/(2*a)

print('A função y = 3x^2 - 4x - 10 tem como raízes,', x_1, 'e', x_2)

#Exercício 4

s=50*(10**(-2))
h=5
ang=s/h

print('O ângulo zenital do sol é,', ang, 'radianos')

#Exercício 5

h_a=1.77
m_a=77
imc_a=m_a/(h_a**2)

h_g=1.75
m_g=80
imc_g=m_g/(h_g**2)

h_bb=0.7
m_bb=11
imc_bb=m_bb/(h_bb**2)

print('O IMC do Augustus é,', imc_a)
print('O IMC do Gabriel é,', imc_g)
print('O IMC do bebê é,', imc_bb)

#Exercício 6

y=0
y_0=3
g=9.8
t_q=(2*(y_0-y)/g)**0.5
v_y=-g*t_q

print('A velocidade final é,', v_y, 'm/s')
print('O tempo de queda é,', t_q, 's')