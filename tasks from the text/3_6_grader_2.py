# Эта программа получает от пользователя количество баллов
# и показывает соответствующий буквенный уровень знаний.

# Именованные константы, представляющие пороги уровней.
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Получить от пользователя баллы за контрольную работу.
score = int(input('Введите баллы за задание: '))

# Определить буквенный уровень.
if score >= A_SCORE:
    print('Ваш уровень - A')
elif score >= B_SCORE:
    print('Ваш уровень - B')
elif score >= C_SCORE:
    print('Ваш уровень - C')
elif score >= D_SCORE:
    print('Ваш уровень - D')
else:
    print('Ваш уровень - F')
