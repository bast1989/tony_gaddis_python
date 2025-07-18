# Эта программа показывает итоговый объем
# продаж из файла sales data.txt.

def main():
    # Инициализировать накопитель.
    total = 0
    try:
        # Открыть файл sales_data.txt.
        infile = open('sales_data.txt', 'r')

        # Прочитать значения из файла
        # и накопить их в переменной.
        for line in infile:
            total += float(line)

        # Закрыть файл.
        infile.close()

        # Напечатать итог.
        print(f'{total:,.2f}')

    except:
        print('Произошла ошибка.')


if __name__ == '__main__':
    main()