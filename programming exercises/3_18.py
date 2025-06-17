REST_1 = 'Центральная пиццерия'
REST_2 = 'Кафе за углом'
REST_3 = 'Блюда от итальянской мамы'
REST_4 = 'Кухня шеф повара'


veget_flag = False
vegan_flag = False
no_glu_flag = False

answer = input('Будет ли на ужине вегетарианец (да/нет): ')
if answer == 'да':
    veget_flag = True

answer = input('Будет ли на ужине веганец (да/нет): ')
if answer == 'да':
    vegan_flag = True

answer = input('Будет ли на ужине приверженец безглютеновой диеты? (да/нет): ')
if answer == 'да':
    no_glu_flag = True

print('Вам подойдёт:')

if veget_flag == True and vegan_flag == False and no_glu_flag == False:
    print(f'{REST_1}, {REST_2}, {REST_3}, {REST_4}')
elif veget_flag == False and vegan_flag == True and no_glu_flag == False:
    print(f'{REST_2}, {REST_4}')
elif veget_flag == False and vegan_flag == False and no_glu_flag == True:
    print(f'{REST_1}, {REST_2}, {REST_4}')
elif veget_flag == True and vegan_flag == True and no_glu_flag == False:
    print(f'{REST_2}, {REST_4}')
elif veget_flag == False and vegan_flag == True and no_glu_flag == True:
    print(f'{REST_2}, {REST_4}')
elif veget_flag == True and vegan_flag == False and no_glu_flag == True:
    print(f'{REST_1}, {REST_2}, {REST_4}')
elif veget_flag == True and vegan_flag == True and no_glu_flag == True:
    print(f'{REST_2}, {REST_4}')
else:
    print(f'{REST_1}, {REST_2}, {REST_3}, {REST_4}')

