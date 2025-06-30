# Эта программа вычисляет длину гипотенузы
# прямоугольного треугольника.
import math

def main():
    a = float(input('Введите длину стороны A: '))
    b = float(input('Введите длину стороны B: '))

    c  = math.hypot(a, b)

    print(f'Длинa гипотенузы составляет {c:.2f}')


if __name__ == '__main__':
    main()