# Эта программа добавляет записи о запасах кофе
# в файл coffee.txt.
def main():
    # Создать переменную для управления циклом.
    another = 'д'

    # Открыть файл coffee.txt file в режиме дозаписи.
    coffee_file = open('coffe.txt', 'a')

    # Добавить записи в файл.
    while another == 'д' or another == 'Д':
        # Получить данные с записью о кофе.
        print('Введите следующие данные о кофе:')
        descr = input('Описание: ')
        qty = int(input('Koличecтвo (в фунтах): '))

        # Добавить данные в файл.
        coffee_file.write(f'{descr}\n')
        coffee_file.write(f'{qty}\n')

        # Определить, желает ли пользователь добавить
        # в файл еще одну запись.
        print('Желаете ли Вы оба вить еще одну запись?')
        another = input('Д = да, все остальное = нет:')

    # Закрыть файл.
    coffee_file.close()


if __name__ == '__main__':
    main()


