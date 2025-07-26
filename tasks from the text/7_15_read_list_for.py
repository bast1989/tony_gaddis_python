# Эта программа считывает содержимое файла в список.

def main():
    # Открыть файл для чтения.
    in_file = open('cities.txt', 'r', encoding='utf-8')

    # Прочитать одержимое файла в список.
    cities = in_file.readlines()

    # Закрыть файл.
    in_file.close()

    # Удалить из каждого элемента символ \n.
    for i in cities:
        cities[cities.index(i)] = i.rstrip('\n')

    # Напечатать содержимое списка.
    print(cities)


if __name__ == '__main__':
    main()


