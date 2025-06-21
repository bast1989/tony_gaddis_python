# Эта программа выводит прямоугольную комбинацию
# звездочек.

rows = int(input('Сколько строк: '))
cols = int(input('Сколько столбцов: '))

for row in range(rows):
    for col in range(cols):
        print('*', end='')
    print()