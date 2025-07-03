import random


START = 0
STOP = 100

def calculate_even_number(num):
    return num % 2 == 0


def main():
    even = 0
    not_even = 0
    for i in range(START, STOP):
        num = random.randint(1, 9999999999)
        if calculate_even_number(num):
            even += 1
        else:
            not_even += 1
    print(f'Четные: {even}')
    print(f'Не четные: {not_even}')


if __name__ == '__main__':
    main()
