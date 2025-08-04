# Эта программа демонстрирует лексемизацию строковых литералов.

# Функция display_tokens выводит на экран лексемы,
# находящиеся в строковом литерале. Параметр data
# является строковым литералом, подлежащим лексемизации,
# а параметр delimiter - разделителем.
def display_token(data, delimiter):
    data_list = data.split(delimiter)

    for token in data_list:
        print(f'Лексема: {token}')

def main():
    # Строковые литералы, подлежащие лексемизации.
    str_1 = 'one two three four'
    str_2 = '10:20:30:40:50:60:70:80:90'
    str_3 = 'a/b/c/d/e/f/g'

    # Вывести на экран лексемы в каждом строковом литерале.
    display_token(str_1, ' ')
    print()
    display_token(str_2, ':')
    print()
    display_token(str_3, '/')


if __name__ == '__main__':
    main()