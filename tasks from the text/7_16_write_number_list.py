# Эта программа сохраняет список чисел в файл.

def main():
    # Создать список чисел.
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Открыть файл для записи.
    out_file = open('nums.txt', 'w')

    # Записать список в файл.
    for i in numbers:
        out_file.write(f'{i}\n')

    # Закрыть файл.
    out_file.close()


if __name__ == '__main__':
    main()

