DAY = 5
total = 0

for i in range(DAY):
    err = int(input(f'Количество ошибок произошедших в день {i + 1}: '))
    total += err

print(f'За {DAY} день(ней,ня) произошло(а,и) {total} ошибка(и,ок)')