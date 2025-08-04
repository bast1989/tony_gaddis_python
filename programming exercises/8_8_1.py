

def main():
    lists = []
    akum = ''
    my_str = input(': ')
    for i in my_str:
        if i.isalnum() or i.isspace():
            akum += i
        else:
            akum += i
            lists.append(akum.strip())
            akum = ''

    print(lists)

if __name__ == '__main__':
    main()