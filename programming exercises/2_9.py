from time import sleep
temperature_c = int(input('Введите температуру в градусах Цельсия: '))
temperature_f = ((9 / 5) * temperature_c) + 32
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print(f'Температура в градусах по Фаренгейту равна {temperature_f:.1f}')