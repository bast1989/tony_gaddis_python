def max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    elif num_1 < num_2:
        return num_2
    else:
        return 'Числа равны'


def main():
    num1 = int(input('Введите число 1: '))
    num2 = int(input('Введите число 2: '))
    print(max(num1, num2))


if __name__ == '__main__':
    main()