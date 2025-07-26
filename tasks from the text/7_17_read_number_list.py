# Эта программа считывает числа из файла в список.

def main():
    # Открыть файл для чтения.
    in_file = open('nums.txt', 'r')

    # Прочитать содержимое файла в список.
    numbers = in_file.readlines()

    # Закрыть файл.
    in_file.close()

    # Конвертировать каждый элемент в тип int.
    i = 0
    while i < len(numbers):
        numbers[i] = int(numbers[i])
        i += 1

    # Напечатать содержимое списка.
    print(numbers)


if __name__ == '__main__':
    main()