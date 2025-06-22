weight = float(input('Введите ваш нынешний вес: '))
MONTH = 6
DOWN_WEIGHT = 1.5

print(f'|{'Месяц':^15}|{'Вес':^15}|')
print('|---------------|---------------|')

for m in range(MONTH):
    weight -= DOWN_WEIGHT
    print(f'|{m + 1:^15}|{weight:^15.2f}|')