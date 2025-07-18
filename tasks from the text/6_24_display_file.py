# Эта программа показывает содержимое
# файла.
from importlib.resources import contents


def main():
    # Получить имя файла.
    name = input('Введите имя файла: ')

    # Открыть файл.
    infile = open(f'{name}.txt', 'r')

    # Прочитать содержимое файла.
    content = infile.read()

    # Показать содержимое файла.
    print(content)

    # Закрыть файл.
    infile.close()


if __name__ == '__main__':
    main()