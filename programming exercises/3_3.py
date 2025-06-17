age = int(input('Введите возраст: '))

if age > 20:
    print('взрослый')
elif age > 13:
    print('подросток')
elif age > 1:
    print('ребёнок')
elif age == 1 or age == 0:
    print('младенец')
else:
    print('нет такого возраста')