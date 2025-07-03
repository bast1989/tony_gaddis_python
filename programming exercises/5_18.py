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
    for end in range(1, 101):
        if is_prime(end):
            print(f'{end} число простое')
        else:
            print(f'{end} число не простое')


if __name__ == '__main__':
    main()
