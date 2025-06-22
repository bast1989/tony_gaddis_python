END = 25
iteration_years = 1
up = 1.6
total_up = 0

print(f'|{'Год':^15}|{'Уровень':^15}|')
print('|---------------|---------------|')

while iteration_years <= END:
    total_up += up
    print(f'|{iteration_years:^15}|{total_up:^15.1f}|')
    iteration_years += 1

