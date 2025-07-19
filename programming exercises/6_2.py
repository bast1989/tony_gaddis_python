COUNT = 5

def main():
    i = 1
    name = input('Имя файла для чтения: ')

    read_file = open(f'{name}.txt', 'r')

    line = read_file.readline()

    while line and i <= COUNT:
        print(line.rstrip('\n'))
        line = read_file.readline()
        i += 1

    read_file.close()


if __name__ == '__main__':
    main()