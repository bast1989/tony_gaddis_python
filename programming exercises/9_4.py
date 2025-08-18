def main():
    words_list = []
    text = open('new_en_text.txt', 'r')

    for line in text:
        words_list += line.strip().split()

    unique_words = set(words_list)


    print('Текст содержит следующий список уникальных слов:')

    for word in unique_words:
        print(word)


if __name__ == '__main__':
    main()