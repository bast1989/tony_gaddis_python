MONTH = 12

year = int(input('Введите количество лет фиксации измерений: '))
total_water = 0

for y in range(year):
    for m in range(MONTH):
        water = float(input(f'Месяц #{m + 1} количество выпавших осадков: '))
        total_water += water

average_water = total_water / (year * MONTH)

print(f'Общее количество осадков за {year * MONTH} месяцев составило: {total_water}',
      f'Среднее количество осадков за {year * MONTH} месяцев составило: {average_water}', sep='\n')
