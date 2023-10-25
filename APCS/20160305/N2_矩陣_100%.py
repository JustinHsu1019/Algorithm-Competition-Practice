# https://zerojudge.tw/ShowProblem?problemid=b965

def change_1(big_list, row, col):
    new_list = []
    for i in range(row-1, -1, -1):
        temp_li = []
        for j in range(col):
            temp_li.append(big_list[i][j])
        new_list.append(temp_li)
    return new_list, len(new_list), len(new_list[0])

def change_2(big_list, row, col):
    new_list = []
    for i in range(col-1, -1, -1):
        temp_li = []
        for j in range(row):
            temp_li.append(big_list[j][i])
        new_list.append(temp_li)
    return new_list, len(new_list), len(new_list[0])

def print_list(result_list):
    result_str = ""
    for i in range(len(result_list)):
        temp_str = ""
        for j in range(len(result_list[0])):
            temp_str = temp_str + result_list[i][j] + " "
        result_str = result_str + temp_str[0:-1] + "\n"
    return result_str[0:-1]

while True:
    try:
        input11 = input()
    except EOFError:
        break

    row = int(input11.split(" ")[0])
    col = int(input11.split(" ")[1])
    _ = int(input11.split(" ")[2])

    big_list = []
    for _ in range(row):
        temp = input()
        col_t = temp.split(" ")
        big_list.append(col_t)

    processinput = input()
    process_list = processinput.split(" ")
    two_list = []
    for i in range(len(process_list)):
        two_list.append(process_list[-1-i])

    for i in two_list:
        if i == "1":
            big_list, row, col = change_1(big_list, row, col)
        elif i == "0":
            big_list, row, col = change_2(big_list, row, col)

    print(str(len(big_list)) + " " + str(len(big_list[0])))
    print(print_list(big_list))
