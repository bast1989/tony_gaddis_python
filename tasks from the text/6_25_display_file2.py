# Эта программа показывает содержимое
# файла.

def main():
    # Получить имя файла.
    name = input('Введите имя файла: ')
    try:
        # Открыть файл.
        infile = open(f'{name}.txt', 'r')

        # Прочитать содержимое файла.
        content = infile.read()

        # Показать содержимое файла.
        print(content)

        # Закрыть файл.
        infile.close()
    except FileNotFoundError:
        print(f'Вызываемый файл {name} не найден.')


if __name__ == '__main__':
    main()