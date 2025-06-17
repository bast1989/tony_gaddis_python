length = float(input('Введите длину гряды: '))
support = float(input('Введите пространство, занимаемое концевой опорой: '))
distance = float(input('Введите расстояние между виноградными лозами в метрах: '))
total_the_vines = (length - 2 * support) / distance
print(f'Количество лоз в такой гряде составит: {total_the_vines:.0f} шт.')