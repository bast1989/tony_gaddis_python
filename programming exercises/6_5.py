def main():
    total = 0
    try:
        num_file = open('number.txt', 'r')
        for i in num_file:
            i = int(i.rstrip('\n'))
            total += i
        num_file.close()
    except Exception as err:
        print(f'Ошибка: {err}')

    print(f'{total}')


if __name__ == '__main__':
    main()