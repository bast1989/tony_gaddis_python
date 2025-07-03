import random


def game(num):
    print(num)
    score = 1
    answer = int(input('Введите число: '))
    while answer != num:
        if answer > num:
            print('Слишком много, попробуйте еще раз')
            score += 1
        else:
            print('Слишком мало, попробуйте еще раз')
            score += 1
        answer = int(input('Введите число: '))
    print(f'Поздравляем вы угадали, на это ушло {score} попыток')

def main():
    while True:
        num = random.randint(1, 100)
        game(num)


if __name__ == '__main__':
    main()
