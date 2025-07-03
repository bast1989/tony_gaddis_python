import random


def printing(num_1, num_2):
    print(f'{'':2}{num_1:>3}')
    print(f'{'+':<2}{num_2:>3}')


def main():
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    printing(num_1, num_2)
    answer = int(input('Введите ответ: '))
    if answer == num_1 + num_2:
        print('Ответ правильный')
    else:
        print(f'Ответ {num_1 + num_2}')


if __name__ == '__main__':
    main()