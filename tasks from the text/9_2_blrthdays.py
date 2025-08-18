# Эта программа применяет словарь для хранения
# имен и дней рождения друзей.

# Глобальные канет.анты для пунктов меню
LOCK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
QUIT = 6


# Функция get_menu_choice выводит меню и получает
# проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('|----------------------|')
    print('1. Найти день рождения')
    print('2. Добавить день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Показать все дни рождения')
    print('6. Выйти из программы')
    print()

    # Получить выбранный пользователем пункт.
    choice = int(input('Введите выбранный пункт: '))

    # Проверить выбранный пункт на допустимость.
    while choice < LOCK_UP or choice > QUIT:
        print('Введёное значение не может быть обработано.')
        choice = int(input('Введите выбранный пункт: '))

    # Вернуть выбранный пользователем пункт.
    return choice


# Функция look_up отыскивает имя
def lock_up(birthdays):
    # Проверить есть ли данные в списке.
    if not len(birthdays):
        print('Нет ни одной записи о днях рождения.')
        print('Сначала нужно внести данные в словарь')
    else:
        # Получить искомое имя.
        name = input('Введите имя: ')
        # Отыскать его в словаре.
        print(birthdays.get(name, 'Имя не найдено с словаре'))


# Функция add добавляет
# в словарь birthdays.
def add(birthdays):
    # Получить имя и день рождения.
    name = input('Введите имя друга для добавления в словарь: ')
    bday = input('Введите его день рождения: ')

    # Если имя не существует, то его добавить.
    if name not in birthdays:
        birthdays[name] = bday
        print('Запись успешно добавлена.')
    else:
        print('Невозможно добавить этот день рождения')
        print('Такая дата уже есть в словаре')
        print('Воспользуйтесь пунктом \'Изменить день рождения\'')


# Функция change изменяет существующую
# запись в словаре birthdays.
def change(birthdays):
    # Получить искомое имя.
    name = input('Введите имя друга что бы изменить его день рождения: ')

    if name in birthdays:
        # Получить новый день рождения.
        bday = input('Введите его день рождения: ')
        # Обновить запись.
        birthdays[name] = bday
        print('Запись успешно изменена.')
    else:
        print('Невозможно изменить этот день рождения')
        print('Такой даты нет в словаре')
        print('Воспользуйтесь пунктом \'Добавить день рождения\'')


# Функция delete удаляет запись из
# словаря birthdays.
def delete(birthdays):
    # Получить искомое имя.
    name = input('Введите имя которое нужно удалить из словаря: ')

    # Если имя найдено, то удалить эту запись.
    if name in birthdays:
        del birthdays[name]
    else:
        print('Имя которое вы хотели удалить не найдено')


def convert_file_to_list():
    bfile = open('birthdays.txt', 'r')
    birthdays = {}
    if not bfile:
        return birthdays
    else:
        name = bfile.readline().strip()
        while name:
            bday = bfile.readline().strip()
            birthdays[name] = bday
            name = bfile.readline().strip()
        return birthdays


def convert_list_to_file(birthdays):
    bfile = open('birthdays.txt', 'w')
    for k, v in birthdays.items():
        bfile.write(f'{k}\n')
        bfile.write(f'{v}\n')
    bfile.close()


def show_all(birthdays):
    for k,v in birthdays.items():
        print(f'Имя друга {k}\nЕго день рождения {v}')


# Главная функция.
def main():
    # Создать пустой словарь.
    birthdays = convert_file_to_list()

    # Инициализировать переменную для выбора пользователя.
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOCK_UP:
            lock_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
        elif choice == SHOW_ALL:
            show_all(birthdays)

    convert_list_to_file(birthdays)


if __name__ == '__main__':
    main()
