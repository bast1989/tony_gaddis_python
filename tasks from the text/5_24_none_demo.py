# Эта программа демонстрирует ключевое слово None.
def get_number():
    print('Введите числа для деления:')
    num_1 = float(input('Введите число 1: '))
    num_2 = float(input('Введите число 2: '))
    return num_1, num_2


def divide(num_1, num_2):
    if num_2 == 0:
        result = None
    else:
        result = num_1 / num_2
    return result


def printing(result):
    if result is None:
        print('Ошибка, на ноль делить нельзя.')
    else:
        print(f'Результат деления равен {result:.2f}')

def main():
    number_1, number_2 = get_number()

    quotient = divide(number_1, number_2)

    printing(quotient)


if __name__ == '__main__':
    main()
