def get_str(str):
    return str.replace('т', 'T')


def main():
    user_string = input('Введите строку: ')

    print(get_str(user_string))

if __name__ == '__main__':
    main()