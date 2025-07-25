# Эта программа присваивает случайные числа
# двумерному списку.
import random

# Константы для строк и столбцов
ROWS = 3
COLS = 4

def main():
    # Создать двумерный список.
    values =[[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    # Заполнить список случайными числами.
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    # Показать случайные числа. 
    print(values)


if __name__ == '__main__':
    main()