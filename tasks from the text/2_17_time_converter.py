# Получить от пользователя количество секунд.
total_second = float(input('Bвeдитe количество секунд: '))

# Получить количество часов.
hours = total_second // 3600

# Получить количество оставшихся минут.
minutes = (total_second // 60) % 60

# Получить количество оставшихся секунд.
seconds = total_second % 60

# Показать результаты.
print('Boт время в часах, минутах и секундах :')
print('Часы :',hours)
print('Минуты: ', minutes)
print('Секунды: ', seconds)