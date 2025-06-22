day = int(input('Введите количество дней: '))
total_salary = 0

print(f'|{'День':^15}|{'Зарплата':^15}|')
print('---------------------------------')

for d in range(day):
    total_salary += (d + 1)
    print(f'|{d + 1:^15}|{total_salary:^15}|')

print(f'Дней отработано: {day} - заработная плата {total_salary // 100} рублей {total_salary % 100} копеек.')