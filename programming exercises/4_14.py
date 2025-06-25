row = 7
col = 7

for r in range(row, 0, -1):
    for c in range(r):
        print('*', end='')
    print()