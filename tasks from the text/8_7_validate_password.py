# Эта программа получает от пользователя пароль
# и проверяет его допустимость.
from login2_8_6 import valid_password

def main():
    # Получить от пользователя пароль.
    password = input('Введите пароль: ')

    while not valid_password(password):
        print('Этот пароль недопустим.')
        password = input('Введите пароль: ')

    print('Это допустимый пароль. ')


if __name__ == '__main__':
    main()