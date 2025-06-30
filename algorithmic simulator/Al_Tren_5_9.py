def times_ten(arg):
    return arg * 10


def main():
    num = int(input('Введите число: '))
    print(f'Число: {num}, работа функции: {times_ten(num)}')


if __name__ == '__main__':
    main()