# Эта программа показывает записи
# из файла coffee.txt.

def main():
    # Открыть файл coffee.txt.
    coffee_file = open('coffe.txt', 'r')

    # Прочитать поле с описанием первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = coffee_file.readline()

        # Удалить \n из описания.
        descr = descr.rstrip('\n')
        qty = qty.rstrip('\n')

        # Показать запись.
        print(f'Описание: {descr}')
        print(f'Количество: {qty}')
        print()

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл.
    coffee_file.close()

if __name__ == '__main__':
    main()