x = 10
y = 3

print("Operadores matematicos")
print('Adição: {}'.format(x + y))
print('Subtraçao: {}'.format(x - y))
print('Multiplicação: {}'.format(x * y))
print('Divisão real: {}'.format(x / y))
print('Divisão exata: {}'.format(x // y))
print('Divisão módulo: {}'.format(x % y))
print('Exponencial: {}'.format(x ** y))

print('-'* 45)
print('Operadores de Comparação')
print('x == y: {}'.format(x == y))
print('x != y: {}'.format(x != y))
print('x > y: {}'.format(x > y))
print('x < y: {}'.format(x < y))
print('x >= y: {}'.format(x >= y))
print('x <= y: {}'.format(x <= y))


print('-'* 45)
print('Operadores de Atribuição')
z = x
z+= 1  # z = z + 1
z-=1 # z =  z -1
z*=2 # z = z * 2
z/=2 # z = z /2
z%=3 # z  = z % 3
x**=2 # x  =  x ** 2
x/=3
print(x)
x =100
x//=3
print(x)

print('-'* 45)
print('AND, OR , NOT')

a = True
b = False
c =True
d =0
e =1

print("a AND b: {}".format(a and b))
print("a AND e: {}".format(a and e))
print("a AND c: {}".format(a and c))
print("a OR b: {}".format(a or b))
print("Not a: {}".format(not a))
print("Not b: {}".format(not b))
print("a AND b: {}".format(a & b))
print("a OR b: {}".format(a | b))

print('-'* 45)
print('IN, NOT IN')
dados2 = ('Fabio', 'Classo', 'fabio.classo@email.com', 'Developer')

print("Fabio" in dados2)
print("fabio" in dados2)
print("fabio" not in dados2)


print('-'* 45)
print('IS,  IS NOT')

x =10
y = 10
z = y
print(x is y)
print(z is y)
print(z is not y)




