# Эта программа позволяет пользователю изменять количество
# в записи файла coffee.txt.

import os # Этот модуль нужен для функций remove и rename.

def main():
    # Создать булеву переменную для использования ее в качестве флага.
    not_found = True

    # Получить искомое значение и новое количество.
    search = input('Введите искомое значение: ')
    new_qty = input('Введите новое количество: ')

    # Открыть исходный файл coffee.txt
    coffe_file = open('coffe.txt', 'r')

    # Открыть временный файл.
    temp_file = open('temp.txt', 'w')

    # Прочитать поле с описанием первой записи.
    discr = coffe_file.readline()

    # Прочитать остаток файла.
    while discr:
        # Прочитать поле с количеством.
        qty = coffe_file.readline()

        # Удалить \n из описания.
        discr = discr.rstrip('\n')
        qty = qty.rstrip('\n')

        # Записать во временный файл либо эту запись,
        # либо новую запись, если эта запись
        # подлежит изменению.
        if search == discr:
            # Записать во временный файл измененную запись.
            temp_file.write(f'{discr}\n')
            temp_file.write(f'{new_qty}\n')

            # Назначить флагу not_found значение False.
            not_found = False
        else:
            # Записать исходную запись во временный файл.
            temp_file.write(f'{discr}\n')
            temp_file.write(f'{qty}\n')

        # Прочитать следующее описание.
        discr = coffe_file.readline()

    # Закрыть файл с данными о кофе и временный файл.
    coffe_file.close()
    temp_file.close()

    # Если искомое значение в файле не найдено,
    # то показать сообщение.
    if not_found:
        print('Запись не была найдена.')
    else:
        print('Запись была найдена и изменена.')

    # Удалить исходный файл coffee.txt.
    os.remove('coffe.txt')
    # Переименовать временный файл.
    os.rename('temp.txt', 'coffe.txt')


if __name__ == '__main__':
    main()