def main():
    text_file = open('text.txt', 'r')
    text_list = text_file.readlines()
    text_file.close()
    total = 0

    for line in text_list:
        word_list = line.split()
        total += len(word_list)


    print(total / len(text_list))



if __name__ == '__main__':
    main()