import random


START = 1
STOP = 500


def main():
    try:
        nums = random.randint(START, STOP)
        num_file = open('numbers.txt', 'w')
        for i in range(nums):
            num = str(random.randint(START, STOP))
            num_file.write(f'{num}\n')
        num_file.close()
        print(f'Сгенерировано {nums} чисел')
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()