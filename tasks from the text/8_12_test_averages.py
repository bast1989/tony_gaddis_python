# Эта программа читает результаты контрольных работ из
# файла CSV и вычисляет средний балл для каждого ученика.

def main():
    # Открыть файл.
    csv_file = open('nambers.csv', 'r')

    # Прочитать строки файла в список.
    lines = csv_file.readlines()

    # Закрыть файл.
    csv_file.close()

    # Обработать строки.
    for line in lines:
        # Получить результаты контрольных работ в виде лексем.
        tokens = line.split(',')

        # Подсчитать общее количество баллов за контрольные работы.
        total = 0
        for token in tokens:
            total += float(token)

        # Вычислить средний балл результатов контрольных работ.
        average = total / len(tokens)
        print(f'Cpeдний балл: {average:.2f}')


if __name__ == '__main__':
    main()