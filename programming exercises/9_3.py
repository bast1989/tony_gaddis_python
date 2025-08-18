def main():
    codes = {
        'A': '!', 'B': '"', 'C': '#', 'D': '$', 'E': '%', 'F': '&',
        'G': "'", 'H': '(', 'I': ')', 'J': '*', 'K': '+', 'L': ',',
        'M': '-', 'N': '.', 'O': '/', 'P': ':', 'Q': ';', 'R': '<',
        'S': '=', 'T': '>', 'U': '?', 'V': '@', 'W': '[', 'X': ']',
        'Y': '^', 'Z': '_',

        'a': '`', 'b': '{', 'c': '|', 'd': '}', 'e': '~', 'f': '§',
        'g': '±', 'h': '£', 'i': '¥', 'j': '¢', 'k': '¤', 'l': '¦',
        'm': '°', 'n': '•', 'o': '¶', 'p': 'ß', 'q': '¿', 'r': '×',
        's': '÷', 't': '©', 'u': '®', 'v': 'µ', 'w': '†', 'x': '‡',
        'y': '∆', 'z': '∞'
    }

    revers_codes = {
    '!': 'A',  '"': 'B',  '#': 'C',  '$': 'D',  '%': 'E',  '&': 'F',
    "'": 'G',  '(': 'H',  ')': 'I',  '*': 'J',  '+': 'K',  ',': 'L',
    '-': 'M',  '.': 'N',  '/': 'O',  ':': 'P',  ';': 'Q',  '<': 'R',
    '=': 'S',  '>': 'T',  '?': 'U',  '@': 'V',  '[': 'W',  ']': 'X',
    '^': 'Y',  '_': 'Z',

    '`': 'a',  '{': 'b',  '|': 'c',  '}': 'd',  '~': 'e',  '§': 'f',
    '±': 'g',  '£': 'h',  '¥': 'i',  '¢': 'j',  '¤': 'k',  '¦': 'l',
    '°': 'm',  '•': 'n',  '¶': 'o',  'ß': 'p',  '¿': 'q',  '×': 'r',
    '÷': 's',  '©': 't',  '®': 'u',  'µ': 'v',  '†': 'w',  '‡': 'x',
    '∆': 'y',  '∞': 'z'
}

    line = ''
    uncoding_line = ''

    with open('en_text.txt', 'r', encoding='utf-8') as text_file:
        text = text_file.read()

    for ch in text:
        if ch in codes:
            line += codes[ch]
        else:
            line += ch

    with open('coding_text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(line)

    with open('coding_text.txt', 'r', encoding='utf-8') as text_file:
        coding_text = text_file.read()

    for ch in coding_text:
        if ch in revers_codes:
            uncoding_line += revers_codes[ch]
        else:
            uncoding_line += ch

    print(uncoding_line)


if __name__ == '__main__':
    main()