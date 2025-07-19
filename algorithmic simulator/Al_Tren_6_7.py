import os


def main():
    delete_name = 'Джон Пецo'
    not_found = True

    stud_file = open('students.txt', 'r')
    tmp_file = open('tmp.txt', 'w')

    name = stud_file.readline()

    while name:
        score = stud_file.readline()

        name = name.rstrip('\n')
        score = score.rstrip('\n')

        if delete_name == name:
            not_found = False
        else:
            tmp_file.write(f'{name}\n')
            tmp_file.write(f'{score}\n')

        name = stud_file.readline()

    stud_file.close()
    tmp_file.close()

    if not_found:
        print(f'Имя {delete_name} не найдено, запись не удалена.')
    else:
        print(f'Имя {delete_name} найдено, запись удалена.')

    os.remove('students.txt')
    os.rename('tmp.txt', 'students.txt')


if __name__ == '__main__':
    main()

