# Эта программа делит одно число на другое.

def main():
    num1 = int(input('Введите число 1:'))
    num2 = int(input('Введите число 2:'))

    # Разделить num1 на num2 и показать результат.
    result = num1 / num2
    print(f'{num1} деленное на {num2} равно {result}')


if __name__ == '__main__':
    main()