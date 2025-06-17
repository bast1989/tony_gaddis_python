MINUTE = 60
HOURS = 3600
DAY = 86400

time = int(input('Введите количество секунд: '))

if time < MINUTE:
    print(f'секунд: {time}')
elif time >= MINUTE and time < HOURS:
    minute = time // MINUTE
    second = time % MINUTE
    print(f'минут: {minute}')
    print(f'секунд: {second}')
elif time >= HOURS and time < DAY:
    hours = time // HOURS
    minute = (time % HOURS) // MINUTE
    second = (time % HOURS) % MINUTE
    print(f'часов : {hours}')
    print(f'минут: {minute}')
    print(f'секунд: {second}')
elif time >= DAY:
    day = time // DAY
    hours = (time % DAY) // HOURS
    minute = ((time % DAY) % HOURS) // MINUTE
    second = ((time % DAY) % HOURS) % MINUTE
    print(f'дней: {day}')
    print(f'часов : {hours}')
    print(f'минут: {minute}')
    print(f'секунд: {second}')
else:
    print('dcghnfcvxhnfdgn')