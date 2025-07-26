ROWS = 3
COLS = 3

def main():
    table = []
    for r in range(ROWS):
        table.append([0] * COLS)

    for r in range(ROWS):
        for c in range(COLS):
            value = int(input(f'Строка {r + 1}. Столбец {c + 1}. Введите значение: '))
            table[r][c] = value

    line_1 = table[0][0] + table[0][1] + table[0][2]
    line_2 = table[1][0] + table[1][1] + table[1][2]
    line_3 = table[2][0] + table[2][1] + table[2][2]
    line_4 = table[0][0] + table[1][0] + table[2][0]
    line_5 = table[0][1] + table[1][1] + table[2][1]
    line_6 = table[0][2] + table[1][2] + table[2][2]
    line_7 = table[0][0] + table[1][1] + table[2][2]
    line_8 = table[2][0] + table[1][1] + table[0][2]

    if line_1 == line_2 == line_3 == line_4 == line_5 == line_6 == line_7 == line_8:
        print('Это квадрат Ло Шу.')


if __name__ == '__main__':
    main()