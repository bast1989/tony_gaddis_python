def get_str(str):
    if str.endswith('.com'):
        return True
    else:
        return False


def main():
    user_string = input('Введите строку: ')

    print(get_str(user_string))

if __name__ == '__main__':
    main()