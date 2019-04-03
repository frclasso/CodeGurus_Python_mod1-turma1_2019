# controle de laços /loop control


def main():
    s = 'This is a string'
    for c in s:
        if c == 'a':
            continue  # pula 'a'
            #break # para execucao
        print(c, end='')


if __name__ == '__main__':
    main()
