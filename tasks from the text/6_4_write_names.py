# Эта программа получает от пользователя три имени
# и пишет их в файл.
def main():
    # Получить три имени.
    name1 = input('Друг №1: ')
    name2 = input('Друг №2: ')
    name3 = input('Друг №3: ')

    # Открыть файл с именем friends.txt.
    infile = open('friends.txt', 'w')

    # Записать имена в файл.
    infile.write(f'{name1}\n')
    infile.write(f'{name2}\n')
    infile.write(f'{name3}\n')

    # Закрыть файл.
    infile.close()

if __name__ == '__main__':
    main()