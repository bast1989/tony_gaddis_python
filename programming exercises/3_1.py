MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

day = int(input('Введите число в диапазоне от 1 до 7: '))

if day == MONDAY:
    print('Введённое число соответствует дню недели: Понедельник')
elif day == TUESDAY:
    print('Введённое число соответствует дню недели: Вторник')
elif day == WEDNESDAY:
    print('Введённое число соответствует дню недели: Среда')
elif day == THURSDAY:
    print('Введённое число соответствует дню недели: Четверг')
elif day == FRIDAY:
    print('Введённое число соответствует дню недели: Пятница')
elif day == SATURDAY:
    print('Введённое число соответствует дню недели: Суббота')
elif day == SUNDAY:
    print('Введённое число соответствует дню недели: Воскресенье')
else:
    print('Число не соответствует ни одному дню недели.')