def main():
    up_ch = 0
    low_ch = 0
    num_ch = 0
    s_ch = 0

    text_file = open('text.txt', 'r')
    text_string = text_file.read()
    text_file.close()

    for ch in text_string:
        if ch == '\n':
            print('Uppi!!!')
        elif ch.isupper():
            up_ch += 1
        elif ch.islower():
            low_ch += 1
        elif ch.isdigit():
            num_ch += 1
        elif not ch.isalpha():
            s_ch += 1
    print(f'В файле больших букв: {up_ch}, маленьких букв: {low_ch}, цифр: {num_ch}, знаков: {s_ch}')




if __name__ == '__main__':
    main()