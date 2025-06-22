num = float(input('Введите число в диапазоне от 1 до 100: '))

while num < 1 or num > 100:
    print('Ошибка ввода.')
    num = float(input('Введите число в диапазоне от 1 до 100: '))

print(num)