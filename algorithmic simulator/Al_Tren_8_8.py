def get_str(str):
    return str[:3]


def main():
    user_string = input('Введите строку: ')

    print(get_str(user_string))

if __name__ == '__main__':
    main()