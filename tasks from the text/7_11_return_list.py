# Эта программа получает серию оценок за лабораторные
# работы и вычисляет среднюю оценку,
# отбрасывая самую низкую.


# Функция get_scores получает от пользователя
# серию оценок и сохраняет их в списке.
# Указанная функция возвращает ссыпку на список.
def get_scores():
    # Создать пустой список.
    test_scores = []

    # Создать переменную для управления циклом.
    again = 'д'

    # Получить от пользователя оценки и добавить их
    # в список.
    while again == 'д':
        value = float(input('Bвeдитe оценку: '))
        test_scores.append(value)

        # Желаете проделать это еще раз?
        print('Жeлaeтe добавить еще одну оценку?')
        again = input('д = да, все остальное = нет: ')
        print()

    return test_scores


# Функция get total принимает список в качестве
# аргумента и возвращает сумму значений
# в списке.
def get_total(value_list):
    # Создать переменную для применения в качестве накопителя.
    total = 0

    # Вычислить сумму значений элементов списка.
    for i in value_list:
        total += i

    # Вернуть сумму.
    return total


def main():
    # Получить от пользователя оценки.
    scores = get_scores()

    # Получить сумму оценок.
    total = get_total(scores)

    # Получить самую низкую оценку.
    low_test = min(scores)

    # Вычесть самую низкую оценку из суммы.
    total -= low_test

    # Вычислить среднее значение. Обратите внимание, что
    # мы делим на количество оценок минус 1, потому что
    # самая низкая оценка была отброшена.
    average = total / (len(scores) - 1)

    # Показать среднее значение.
    print(f'Cpeдняя оценка с учетом отброшенной самой низкой оценки: {average}')


if __name__ == '__main__':
    main()