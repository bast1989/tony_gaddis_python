def main():
    # Создать список с несколькими значениями.
    food = ['Пицца', 'Чипсы', 'Бургеры']

    # Показать список.
    print('Boт значения списка продуктов в питания:')
    for i in food:
        print(i)

    # Получить значение, подлежащие изменению.
    item = input('Какое значение следует изменить: ')

    try:
        item_index = food.index(item)
        new_item = input('Введите новое значение: ')
        food[item_index] = new_item

        print('Вот обновлённый список:')
        for i in food:
            print(i)
    except ValueError as err:
        print(f'Этo значение в списке не найдено. \nОшибка: {err}')


if __name__ == '__main__':
    main()