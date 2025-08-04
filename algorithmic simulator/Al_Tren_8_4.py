def main():
    user_string = input('Введите строку: ')
    count = 0

    for ch in user_string:
        if ch.islower():
            count += 1

    print(count)


if __name__ == '__main__':
    main()