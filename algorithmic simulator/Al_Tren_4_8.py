num = float(input('Введите положительное ненулевое число: '))

while num <= 0:
    print('Ошибка ввода.')
    num = float(input('Введите положительное ненулевое число: '))

print(num)