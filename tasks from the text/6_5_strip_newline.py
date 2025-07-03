# Эта программа читает содержимое файла
# philosophers.txt построчно.
def main():
    # Открыть файл с именем philosophers.txt.
    text = open('philosophers.txt', 'r')

    # Прочитать три строки из файла.
    line1 = text.readline()
    line2 = text.readline()
    line3 = text.readline()

    # Удалить \n из каждого строкового значения.
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    # Закрыть файл.
    text.close()

    # Напечатать данные, прочитанные в оперативную память.
    print(line1)
    print(line2)
    print(line3)


if __name__ == '__main__':
    main()