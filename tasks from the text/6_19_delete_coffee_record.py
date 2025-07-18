# Эта программа позволяет пользователю удалить
# запись из файла coffee.txt.
import os # Этот модуль нужен для функций remove и rename.

def main():
    # Создать булеву переменную для использования ее в качестве флага.
    not_found = True

    # Получить бренд кофе, который нужно удалить.
    search = input('Какой бренд желаете удалить? ')

    # Открыть исходный файл coffee.txt.
    coffe_file = open('coffe.txt', 'r')

    # Открыть временный файл.
    temp_file = open('temp.txt', 'w')

    # Прочитать поле с описанием первой записи.
    descr = coffe_file.readline()

    # Прочитать остаток файла.
    while descr:
        # Прочитать поле с количеством.
        qty = coffe_file.readline()

        # Удалить \n из описания.
        descr = descr.rstrip('\n')
        qty = qty.rstrip('\n')

        # Если эта запись предназначена для удаления
        if search == descr:
            # Назначить флагу not_found значение False.
            not_found = False
        # Иначе эта запись не предназначена для удаления,
        # то записать ее во временный файл.
        else:
            # Поместить запись во временный файл.
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        # Прочитать следующее описание.
        descr = coffe_file.readline()

    # Закрыть файл с данными о кофе и временный файл.
    coffe_file.close()
    temp_file.close()

    # Удалить исходный файл coffee.txt.
    os.remove('coffe.txt')
    # Переименовать временный файл.
    os.rename('temp.txt', 'coffe.txt')

    # Если искомое значение в файле не найдено,
    # то показать сообщение.
    if not_found:
        print('Значение в файле не найдено ')
    else:
        print('Значение удалено, файл обновлён.')


if __name__ == '__main__':
    main()
