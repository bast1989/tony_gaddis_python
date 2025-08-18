def main():
    phonebook = {
        'Крис':'919-555-1111',
        'Кэти':'828-919-2222',
        'Джоанна': '704-555-3333',
        'Курт': '919-555-3333'
    }

    filter_phonebook = {k:v for k,v in phonebook.items() if v[:3] == '919'}
    print(filter_phonebook)


if __name__ == '__main__':
    main()