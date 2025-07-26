import random


def main():
    response_file = open('8_ball_responses_ru.txt', 'r')
    response_list = [i.rstrip('\n') for i in response_file]
    response_file.close()

    answer = 'д'

    while answer == 'д':
        request = input('Введи интересующий вас вопрос:\n')
        print('Магический шар ответил вам: ')
        print(random.choice(response_list))
        answer = input('Хотите продолжить?')


if __name__ == '__main__':
    main()