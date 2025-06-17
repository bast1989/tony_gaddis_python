BASE_HOURS = 40
OT_MULTIPLIER = 1.5

name = input('Введите имя сотрудника: ')
hours = int(input('Введите количество отработанных часов: '))
h_rate = float(input('Введите почасовую ставку: '))

if hours > BASE_HOURS:
    overtime = hours - BASE_HOURS
    total = BASE_HOURS * h_rate + overtime * h_rate * OT_MULTIPLIER
else:
    total = hours * h_rate

print(f'Сотруднику {name} за {hours} час(а,ов) начислить до удержания налогов: {total:,.2f}')