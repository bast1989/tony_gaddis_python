iterator_1 = 1
iterator_2 = 30
total = 0

while iterator_2 != 0:
    total += iterator_1 / iterator_2
    iterator_1 += 1
    iterator_2 -= 1

print(f'Нарастающий итог равен: {total:.2f}',
      'Конец выполнения программы', sep='\n')