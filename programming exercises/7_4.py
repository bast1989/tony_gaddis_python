NUMBERS = 20

def main():
    user_nums = []
    total_sum_num = 0
    for i in range(NUMBERS):
        value = int(input(f'Введите число #{i + 1}: '))
        user_nums.append(value)
        total_sum_num += value

    average_num = total_sum_num / NUMBERS
    min_num = min(user_nums)
    max_num = max(user_nums)

    print(f'наименьшее число в списке {min_num}')
    print(f'наибольшее число в списке {max_num}')
    print(f'сумму чисел в списке {total_sum_num}')
    print(f'среднее арифметическое значение чисел в списке {average_num}')


if __name__ == '__main__':
    main()