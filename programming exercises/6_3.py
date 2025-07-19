def main():
    line = 1
    name = input('Введите имя файла: ')
    try:
        read_file = open(f'{name}.txt', 'r')
        for i in read_file:
            i = i.rstrip('\n')
            print(f'{line}: {i}')
            line += 1
    except Exception as err:
        print(f'Ошибка: {err}')
    finally:
        read_file.close()

if __name__ == '__main__':
    main()