def main():
    check_file = open('check_list.txt', 'r')
    check_list = check_file.readlines()
    check_file.close()
    check_list = [i.rstrip('\n') for i in check_list]
    stud_file = open('student_solution.txt', 'r')
    stud_list = stud_file.readlines()
    stud_file.close()
    stud_list = [i.rstrip('\n') for i in stud_list]

    score = 0

    if len(check_list) == len(stud_list):
        for i in range(len(check_list)):
            if check_list[i] == stud_list[i]:
                score += 1

    if score >= 15:
        print('Вы прошли тест.')
    else:
        print('Вы не прошли тест')


if __name__ == '__main__':
    main()