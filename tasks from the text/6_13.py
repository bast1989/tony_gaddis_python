from faker import Faker

def main():
    fake = Faker('ru_RU')
    staff = int(input('Введите количество сотрудников для генерации: '))
    staff_file = open('staff_company.txt', 'w')

    for i in range(staff):
        staff_file.write(f'{fake.name()}\n')
        staff_file.write(f'{fake.job()}\n')
        staff_file.write(f'{fake.postcode()}\n')

    staff_file.close()

if __name__ == '__main__':
    main()