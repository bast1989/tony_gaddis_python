# Эта программа помогает лаборанту в процессе
# контроля температуры вещества.

# Именованная константа, которая представляет максимальную
# температуру.

MAX_TEMP = 102.5

# Получить температуру вещества.
temperature = float(input('Bвeдитe температуру вещества в градусах Цельсия: '))

# Пока есть необходимость, инструктировать пользователя
# в корректировке нагрева.

while temperature > MAX_TEMP:
    print('Температура слишком высокая.')
    print('Убавьте нагрев и подождите')
    print('5 минут. Затем снимите показания температуры')
    print('снова и введите значение.')
    temperature = float(input('Bвeдитe температуру вещества в градусах Цельсия: '))

# Напомнить пользователю проконтролировать температуру сн ва
# через 15 минут.


print('Температура приемлемая')
print('Проверьте её снова через 15 минут.')