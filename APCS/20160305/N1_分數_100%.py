# https://zerojudge.tw/ShowProblem?problemid=b964

while True:
    try:
        student_num = int(input())
    except EOFError:
        break
    studentinp = input()
    student_list = studentinp.split(" ")
    for i in range(len(student_list)):
        student_list[i] = int(student_list[i])
    student_list = sorted(student_list)
    result_str = ""
    great = []
    nope = []
    for i in range(len(student_list)):
        result_str = result_str + str(student_list[i]) + " "
        if 0 <= student_list[i] < 60:
            nope.append(student_list[i])
        elif 60 <= student_list[i] <=100:
            great.append(student_list[i])

    print(result_str[0:-1])
    nope = sorted(nope)
    great = sorted(great)
    if nope == []:
        print("best case")
    else:
        print(nope[-1])

    if great == []:
        print("worst case")
    else:
        print(great[0])
