mass = int(input('Введите массу тела в килограммах: '))

weight = mass * 9.8

print(f'Вес тела равен: {weight:.2f} ньютон(а,ов)')
if weight > 500:
    print('Тело слишком тяжёлое')
elif weight < 100:
    print('Тело слишком лёгкое')
