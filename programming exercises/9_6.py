def unique_words_generator(file):
    punctuation = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
        '{', '|', '}', '~'
    ]

    text = file.read()

    words_list = text.split()

    for word in words_list:
        if word[-1] in punctuation:
            new_word = word[:-1].lower()
            words_list[words_list.index(word)] = new_word
        else:
            new_word = word.lower()
            words_list[words_list.index(word)] = new_word

    return set(words_list)


def main():

    text_file_1 = open('text_file_1.txt', 'r')
    unique_words_1 = unique_words_generator(text_file_1)
    text_file_1.close()

    text_file_2 = open('text_file_2.txt', 'r')
    unique_words_2 = unique_words_generator(text_file_2)
    text_file_2.close()

    print('В списке:')
    print(f'Уникальных слов в обоих файлах: {unique_words_1.union(unique_words_2)}')
    print(f'Слов, входящих в оба файла: {unique_words_1.intersection(unique_words_2)}')
    print(f'Слов из первого файла, не входящих во второй: {unique_words_1.difference(unique_words_2)}')
    print(f'Слов из второго файла, не входящих в первый: {unique_words_2.difference(unique_words_1)}')
    print(f'Слов входящих либо в первый, либо во второй файл, но не входящих в оба файла одновременно. {unique_words_1.symmetric_difference(unique_words_2)}')


if __name__ == '__main__':
    main()