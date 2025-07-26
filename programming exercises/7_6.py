import random


NUMBERS = 20
START_NUM = 0
STOP_NUM = 100

def get_f_num(num, num_list):
    return [i for i in num_list if i > num]



def main():
    random_numbers = []
    for i in range(NUMBERS):
        random_numbers.append(random.randint(START_NUM, STOP_NUM))

    filter_value = int(input('Введите число для фильтрации: '))

    print(random_numbers)

    print(get_f_num(filter_value, random_numbers))


if __name__ == '__main__':
    main()