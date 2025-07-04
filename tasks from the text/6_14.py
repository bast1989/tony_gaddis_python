def main():
    staff_file = open('staff_company.txt', 'r')
    count  = 0
    name = staff_file.readline().rstrip('\n')

    while name != '':
        count += 1
        job = staff_file.readline().rstrip('\n')
        name_id = staff_file.readline().rstrip('\n')
        print(f'Информация о сотруднике #{count}:')
        print(f'Имя: {name}')
        print(f'Профессия: {job}')
        print(f'Идентификационный номер: {name_id}')
        print()
        name = staff_file.readline().rstrip('\n')

    staff_file.close()

if __name__ == '__main__':
    main()