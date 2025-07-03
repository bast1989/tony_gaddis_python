# Эта программа читает и показывает содержимое
# файла philosophers.txt.
def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Прочитать содержимое файла.
    file_content = infile.read()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, считанные
    # в оперативную память.
    print(file_content)

if __name__ == '__main__':
    main()
