def sum(num_1, num_2):
    result = num_1 + num_2
    return result

def main():
    first_age = int(input('Введите число 1:'))
    second_age = int(input('Введите число 2:'))

    total = sum(first_age, second_age)
    print(total)

if __name__ == '__main__':
    main()