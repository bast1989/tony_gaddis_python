# Эта программа демонстрирует функцию sqrt.
import math

def main():
    number = float(input('Введите число: '))

    square_root = math.sqrt(number)

    print(f'Корень из {number} равняется {square_root}')


if __name__ == '__main__':
    main()