def main():
    full_name = input('Введите ФИО:')
    f_name_list = full_name.split(' ')

    print(f'Ваши инициалы: {f_name_list[0][0]}{f_name_list[1][0]}{f_name_list[2][0]}')


if __name__ == '__main__':
    main()