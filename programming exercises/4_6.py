START_C = 0
END_C = 21

print(f'|{'Цельсий':^15}|{'Фаренгейт':^15}|')
print('---------------------------------')

for i in range(START_C, END_C):
    fahrenheit = (9 / 5) * i + 32
    print(f'|{i:^15}|{fahrenheit:^15.1f}|')