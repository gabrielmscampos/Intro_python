print('----------------')
print('Aula 4')
print('----------------')

print('\ndo_twice Example\n')

def do_twice(f):
	f()
	f()

def print_spam():
	print('spam example')

do_twice(print_spam)

print('\ndo_twice Modified\n')

def do_twice(f,x):
	f(x)
	f(x)

def print_spam(x):
	print(x)

x = 'spam modified'
do_twice(print_spam, x)

print('\nprint_twice Generalized\n')

def print_twice(y):
	print(y)
	print(y)

y = 'spam generalized'
do_twice(print_twice, y)

print('\ndo_four Exercise\n')

def do_four(f,x):
	do_twice(f,x)
	do_twice(f,x)

z = 'spam'
do_four(print_twice,z)

print('\nSquare exercise\n')

def print_linhas(x):
	print(x)

def print_coluna(x):
	print(x)

def print_grid():
	print_linhas(x1)
	do_four(print_coluna, x2)
	print_linhas(x1)
	do_four(print_coluna, x2)
	print_linhas(x1)

x1 = '+ - - - - + - - - - +'
x2 = '|         |         |'
print_grid()