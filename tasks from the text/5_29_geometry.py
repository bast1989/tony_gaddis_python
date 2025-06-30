# Эта программа позволяет пользователю выбирать различные
# геометрические вычисления из меню.
# Программа импортирует модули circle и rectangle
import circle_5_27
import rectangle_5_28

# Константы для элементов меню.
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# Функция display_menu показывает меню.
def display_menu():
    print(' МЕНЮ')
    print('1. Площадь круга')
    print('2. Длина окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямоугольника')
    print('5. Выход')


def main():
    # Переменная choice управляет циклом
    # и содержит вариант выбора пользователя.
    choice = 0

    while choice != QUIT_CHOICE:
        # Показать меню.
        display_menu()

        # Получить вариант выбора пользователя.
        choice = int(input('Введите пункт меню: '))

        # Выполнить выбранное действие.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            result = circle_5_27.area(radius)
            print(f'Площадь круга равна: {result:.2f}')
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            result = circle_5_27.circumference(radius)
            print(f'Длина окружности равна: {result:.2f}')
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длину прямоугольника: '))
            result = rectangle_5_28.area(width, length)
            print(f'Площадь прямоугольника равна: {result:.2f}')
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длину прямоугольника: '))
            result = rectangle_5_28.perimeter(width, length)
            print(f'Площадь прямоугольника равна: {result:.2f}')
        elif choice == QUIT_CHOICE:
            print('Программа завершена.')
        else:
            print('Ошибка ввода')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()


