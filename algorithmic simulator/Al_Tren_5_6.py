import random

def generate_random_number():
    num = random.randint(1, 100)
    return num


def main():
    rand = generate_random_number()
    print(rand)


if __name__ == '__main__':
    main()