def main():
    accounts_file = open('charge_accounts.txt', 'r')
    accounts_list = accounts_file.readlines()
    accounts_file.close()

    accounts_list = [int(i.rstrip('\n')) for i in accounts_list]

    search_accounts = int(input('Введите расходный счёт компании: '))

    if search_accounts in accounts_list:
        print('Номер допустимый.')
    else:
        print('Номер недопустимый.')


if __name__ == '__main__':
    main()