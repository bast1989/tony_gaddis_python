def main():
    user_string = input('Введите строку: ')
    count = 0

    for i in user_string:
        if i in ' ':
            count += 1

    print(count)


if __name__ == '__main__':
    main()
