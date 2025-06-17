years = int(input('Введите год: '))

if years % 100 == 0 and years % 400 == 0:
    print(f'год {years} является високосным')
elif years % 100 != 0 and years % 4 == 0:
    print(f'год {years} является високосным')
else:
    print(f'год {years} не является високосным')