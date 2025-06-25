num = int(input('Введите число: '))
factorial = 1
message = ''

if num < 0:
    message = 'Факториал не определён для отрицательных чисел.'
elif num == 1 or num == 0:
    message = f'Факториал числа {num} равен {factorial}'
else:
    for i in range(2, num + 1):
        factorial *= i
        message = f'Факториал числа {num} равен {factorial}'

print(message)
