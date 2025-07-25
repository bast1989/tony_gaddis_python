# Эта программа применяет цикл for дпя чтения
# всех значений из файла sales.txt.
def main():
    # Открыть файл sales.txt дпя чтения.
    sales_file = open('sales.txt', 'r')

    # Прочитать все троки из файла.
    for line in sales_file:
        # Конвертировать строку в число с плавающей очкой .
        amount = float(line)
        # Отформатировать и показать сумму.
        print(f'{amount:,.2f}')

    # Закрыть файл.
    sales_file.close()


if __name__ == '__main__':
    main()