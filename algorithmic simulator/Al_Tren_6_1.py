def main():
    name = 'Alex Ofmark'

    name_file = open('my_name.txt', 'w')

    name_file.write(f'{name}\n')

    name_file.close()

    
if __name__ == '__main__':
    main()