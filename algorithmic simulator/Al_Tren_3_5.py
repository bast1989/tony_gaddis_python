amount1 = int(input('Введите первое число: '))
amount2 = int(input('Введите второе число: '))

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(f'Большее значение мз двух {amount1}')
    else:
        print(f'Большее значение мз двух {amount2}')
else:
    print('Что то пошло не так, извините.')