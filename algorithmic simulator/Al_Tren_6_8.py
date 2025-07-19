import os


def main():
    change_name = 'Джулия Динтон'
    new_score = 100
    not_found = True

    stud_file = open('students.txt', 'r')
    tmp_file = open('tmp.txt', 'w')

    name = stud_file.readline()

    while name:
        score = stud_file.readline()

        name = name.rstrip('\n')
        score = score.rstrip('\n')

        if change_name == name:
            tmp_file.write(f'{name}\n')
            tmp_file.write(f'{new_score}\n')
            not_found = False
        else:
            tmp_file.write(f'{name}\n')
            tmp_file.write(f'{score}\n')

        name = stud_file.readline()

    stud_file.close()
    tmp_file.close()

    if not_found:
        print(f'Имя {change_name} не найдено, запись не изменена.')
    else:
        print(f'Имя {change_name} найдено, запись изменена.')

    os.remove('students.txt')
    os.rename('tmp.txt', 'students.txt')


if __name__ == '__main__':
    main()

