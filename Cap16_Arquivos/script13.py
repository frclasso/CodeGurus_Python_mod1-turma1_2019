
# read, readline, readlines

# seek (posiciona o cursor), tell (diz onde esta o cursor)

fo = open('foo2.txt', 'r')
line = fo.read(30)
print(line)
print(fo.tell()) # posicao

print()
fo.seek(0)  # inicio
print(fo.tell()) # posicao
line = fo.read()
print(line)
print(fo.tell())




# line = fo.readline()
#line = fo.readlines()

