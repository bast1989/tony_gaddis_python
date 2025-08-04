# Эта программа вызывает метод split, используя
# символ '/' в качестве разделителя.

def main():
    # Создать строковое значение с датой.
    date_string = '21/12/1989'

    # Разбить дату.
    date_list = date_string.split('/')

    # Показать все части даты.
    print(f'День: {date_list[0]}')
    print(f'Месяц: {date_list[1]}')
    print(f'Год: {date_list[2]}')


if __name__ == '__main__':
    main()