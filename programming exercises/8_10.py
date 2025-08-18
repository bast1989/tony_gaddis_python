def main():
    line = input('Введите строку: ')
    line_list = list(line.lower())
    line_set = tuple(set(line_list))
    line_num_count = []
    count = 0

    for ch in line_set:
        while ch in line_list:
            line_list.remove(ch)
            count += 1
        line_num_count.append(count)
        count = 0


    max_count = max(line_num_count)
    print(f'В ваше фразе {max_count} букв: ')
    print(f'{line_set[line_num_count.index(max_count)]}')

    print(line_set)
    print(line_num_count)

if __name__ == '__main__':
    main()