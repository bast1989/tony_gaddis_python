# Эта программа демонстрирует применение метода append
# для добавления значений в список.

def main():
    # Сначала создать пустой список.
    name_list = []

    # Создать переменную для управления циклом.
    again = 'д'

    # Добавить в список несколько имен.
    while again == 'д':
        # Получить от пользователя имя.
        name = input('Введите имя: ')

        # Добавить имя в конец списка.
        name_list.append(name)

        # Добавить еще одно?
        print('Желаете добавить еще одно имя?')
        again = input('д = да, все остальное = нет: ')
        print()

    # Показать введенные имена.
    print('Вот имена, которые были введены: ')

    for name in name_list:
        print(name)


if __name__ == '__main__':
    main()