# Эта программа выводит ступенчатую комбинацию.
BASE_SIZE = 6

for r in range(BASE_SIZE):
    for c in range(r):
        print(' ', end='')
    print('#')
