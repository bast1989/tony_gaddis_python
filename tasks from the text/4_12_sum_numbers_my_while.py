END = 5
i = 0
total = 0

while i < END:
    number = float(input(f'Введите число №{i + 1}:'))
    total += number
    i += 1

print(f'Сумма всех введённых вами чисел составляет: {total}')