START = 2


def is_prime(num):
    flag = True
    for i in range(START, num):
        if num % i != 0:
            flag = True
        else:
            return False
    return flag



def main():
    end = int(input('Введите число для проверки: '))
    if is_prime(end):
        print('Число простое')
    else:
        print('Число не простое')


if __name__ == '__main__':
    main()
