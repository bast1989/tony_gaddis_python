score = int(input('Введите количество балов: '))

A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60


if score >= A_SCORE:
    print('Ваш уровень - A')
else:
    if score >= B_SCORE:
        print('Ваш уровень - B')
    else:
        if score >= C_SCORE:
            print('Ваш уровень - C')
        else:
            if score >= D_SCORE:
                print('Ваш уровень - D')
            else:
                print('Ваш уровень - F')