color_1 = input('Введите цвет 1: ')
color_2 = input('Введите цвет 2: ')

check_color_1 = False
check_color_2 = False

if color_1 == 'красный' or color_1 == 'синий' or color_1 == 'желтый':
    check_color_1 = True

if color_2 == 'красный' or color_2 == 'синий' or color_2 == 'желтый':
    check_color_2 = True

if check_color_1 and check_color_2:
    if (color_1 == 'красный' and color_2 == 'синий') or (color_1 == 'синий' and color_2 == 'красный'):
        print('Получился фиолетовый цвет')
    elif (color_1 == 'красный' and color_2 == 'желтый') or (color_1 == 'желтый' and color_2 == 'красный'):
        print('Получился оранжевый цвет')
    elif (color_1 == 'синий' and color_2 == 'желтый') or (color_1 == 'желтый' and color_2 == 'синий'):
        print('Получился зелёный цвет')
else:
    print('Введён не корректный цвет')
