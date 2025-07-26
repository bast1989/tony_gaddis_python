ROWS = 5
COLS = 3

def main():
    n_list = []

    for r in range(ROWS):
        n_list.append([0] * COLS)

    for r in range(ROWS):
        for c in range(COLS):
            print(f'Позиция элемента:\nстрока: {r + 1}\nстолбец: {c + 1}')
            num = int(input('Введите значение элемента: '))
            n_list[r][c] = num

    print(n_list)




if __name__ == '__main__':
    main()