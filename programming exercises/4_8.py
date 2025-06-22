num = 0
total_num = 0

while num >= 0:
    total_num += num
    num = float(input('Введите положительное число для суммирования или отрицательное для выхода из программы: '))

print(f'Сумма введённых чисел равна: {total_num}')