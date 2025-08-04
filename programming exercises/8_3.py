def main():
    date = input('Введите дату в формате: дд/мм/гггг. ')
    # date = '21/12/1989'
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    date_list = date.split('/')

    print(f'{date_list[0]} {months[int(date_list[1]) - 1]} {date_list[2]}')


if __name__ == '__main__':
    main()