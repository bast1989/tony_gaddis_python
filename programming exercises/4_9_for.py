END = 25
up = 1.6
total_up = 0

print(f'|{'Год':^15}|{'Уровень':^15}|')
print('|---------------|---------------|')

for i in range(END):
    total_up += up
    print(f'|{i + 1:^15}|{total_up:^15.1f}|')
