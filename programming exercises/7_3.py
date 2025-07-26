MONTHS = 12

def main():
    precipitation_levels = []
    total = 0

    for i in range(MONTHS):
        values = float(input(f'Введите количество осадков за месяц {i + 1}: '))
        precipitation_levels.append(values)
        total += values

    print(f'Количество осадкой за год: {total:.2f}')
    print(f'Среднее количество осадков в месяц: {total / MONTHS:.2f}')
    print(f'Месяц с наименьшим количеством осадков: {precipitation_levels.index(min(precipitation_levels)) + 1}')
    print(f'Месяц с наибольшим количеством осадков: {precipitation_levels.index(max(precipitation_levels)) + 1}')


if __name__ == '__main__':
    main()