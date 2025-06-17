num = int(input('Введите номер кармана рулетки: '))
red = 'Красное'
black = 'Чёрное'
green = 'Зелёное'

if num >= 29 and num <= 36:
    if num % 2 == 0:
        print(f'{num} {red}')
    else:
        print(f'{num} {black}')
elif num >= 19 and num <= 28:
    if num % 2 == 0:
        print(f'{num} {black}')
    else:
        print(f'{num} {red}')
elif num >= 11 and num <= 18:
    if num % 2 == 0:
        print(f'{num} {red}')
    else:
        print(f'{num} {black}')
elif num >= 1 and num <= 10:
    if num % 2 == 0:
        print(f'{num} {black}')
    else:
        print(f'{num} {red}')
elif num == 0:
    print(f'{num} {green}')
else:
    print('Что то пошло не так, извините.')