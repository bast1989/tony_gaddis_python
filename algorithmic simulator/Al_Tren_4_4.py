END = 10
total = 0

for i in range(END):
    print(f'Итерация #{i + 1} введите число для аккумуляции', end='')
    num = float(input(': '))
    total += num

print(f'Нарастающий итог равен: {total}',
      'Конец выполнения программы', sep='\n')