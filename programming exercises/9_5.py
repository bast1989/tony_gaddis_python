def main():
    punctuation = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
        '{', '|', '}', '~'
    ]

    status_word = dict()

    count = 0

    text_file = open('new_en_text.txt', 'r')

    text = text_file.read()
    words_list = text.split()

    for word in words_list:
        if word[-1] in punctuation:
            new_word = word[:-1]
            words_list[words_list.index(word)] = new_word

    unique_words = set(words_list)

    for s_word in unique_words:
        for l_word in words_list:
            if s_word == l_word:
                count += 1

        status_word[s_word] = count
        count = 0

    for k,v in status_word.items():
        print(f'{k}: {v}')




if __name__ == '__main__':
    main()