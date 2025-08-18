def main():
    auditorium = {
        'CS101': 3004,
        'CS102': 4501,
        'CS103': 6755,
        'CS104': 1244,
        'CS105': 1411
    }

    teacher = {
        'CS101': 'Хайнс',
        'CS102': 'Альварадо',
        'CS103': 'Рич',
        'CS104': 'Берк',
        'CS105': 'Ли'
    }

    time = {
        'CS101': '8:00',
        'CS102': '9:00',
        'CS103': '10:00',
        'CS104': '11:00',
        'CS105': '13:00'
    }

    print('У нас представлены курсы:')

    for i in auditorium:
        print(i)

    course = input('Введите номер курса что бы узнать подробности: ')
    print(f'Курс {course}')
    print(f'Аудитория {auditorium.get(course, "Не найдено")}')
    print(f'Преподаватель {teacher.get(course, "Не найдено")}')
    print(f'Время {time.get(course, "Не найдено")}')


if __name__ == '__main__':
    main()