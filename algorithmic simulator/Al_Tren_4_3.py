START = 0
STOP = 1001
STEP = 10

for i in range(START, STOP, STEP):
    if i != 1000:
        print(f'{i}, ', end='')
    else:
        print(i)