# Эта программа демонстрирует двумерный список.

def main():
    # Создать двумерный список
    values = [[1, 2, 3],
              [10, 20, 30],
              [100, 200, 300]]

    # Вывести на экран элементы списка.
    for row in values:
        for element in row:
            print(element)


if __name__ == '__main__':
    main()


