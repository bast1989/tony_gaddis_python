def get_capitalize_strint(str):
    split_list = ['!', '?', '.']
    accum = ''
    for ch in str:
        if ch.isalnum() or ch.isspace():
            accum += ch
        else:
            accum += ch
            print(accum.strip().capitalize(), end=' ')
            accum = ''

def main():
    my_str = input('Введите строку: ')
    get_capitalize_strint(my_str)

if __name__ == '__main__':
    main()