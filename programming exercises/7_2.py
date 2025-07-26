import random

NUMS = 7
START_NUM = 0
END_NUM = 9

def main():
    lottery_numbers = []
    for n in range(NUMS):
        lottery_numbers.append(random.randint(START_NUM, END_NUM))

    print('Выйгрышный номер лотерейного билета:')

    for n in lottery_numbers:
        print(f'{n}  ', end='')


if __name__ == '__main__':
    main()