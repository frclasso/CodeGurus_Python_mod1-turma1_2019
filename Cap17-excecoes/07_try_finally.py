

try:
    fh = open('test.txt', 'r')
    try:
        fh.read()
    finally:
        print("Fechando...")
        fh.close()
except IOError:
    print('Error - Nao foi possivel encontrar o arquivo')