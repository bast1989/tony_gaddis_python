# Эта программа демонстрирует преобразование
# числовых значений в строковые перед их
# записью в текстовый файл.
def main():
    # Открыть файл для записи.
    outfile = open('numbers.txt', 'w')

    # Получить от пользователя три числа.
    num1 = int(input('Введите число 1: '))
    num2 = int(input('Введите число 2: '))
    num3 = int(input('Введите число 3: '))

    # Записать эти числа в файл.
    outfile.write(f'{num1}\n')
    outfile.write(f'{num2}\n')
    outfile.write(f'{num3}\n')

    # Закрыть файл.
    outfile.close()

if __name__ == '__main__':
    main()
