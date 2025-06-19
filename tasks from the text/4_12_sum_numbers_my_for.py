total = 0

for i in range(5):
    number = float(input(f'Введите число №{i + 1}:'))
    total += number

print(f'Сумма всех введённых вами чисел составляет: {total}')