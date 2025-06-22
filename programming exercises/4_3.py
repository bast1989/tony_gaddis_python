budget = float(input('Введите бюджет на месяц: '))
categories = int(input('Введите количество категорий для списания из бюджета: '))

for i in range(categories):
    name = input(f'Введите название категории #{i + 1}: ')
    expenses = float(input(f'Расходы по категории {name} составили: '))
    budget -= expenses

if budget > 0:
    print(f'В этом месяце экономия составила: {budget:,.2f}')
elif budget < 0:
    print(f'В этом месяце перерасход составил: {budget:,.2f}')
else:
    print('Месяц закончился в 0')