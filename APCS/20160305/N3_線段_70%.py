# https://zerojudge.tw/ShowProblem?problemid=b966

while True:
    try:
        how_many = int(input())
    except EOFError:
        break

    # 處理輸入
    input_list = []
    for i in range(how_many):
        tempstr = input()
        temp = tempstr.split(" ")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        input_list.append(temp)

    # 跑一個三層迴圈
    # 為每一個列表都去跟所有列表做檢查，如果可以合併，就合併
    # 並中斷迴圈，重跑一次新的合併後的列表，直到沒得合併

    # 可以合併的情況: 有重疊
    # 判斷有重疊的方式: 包含在內, 重疊左邊, 重疊右邊
    # 包含在內: List2的第一個數大於List1第一個數, List2第二個數小於List1第二個數
    # 重疊左邊: List2的第一個數小於List1第一個數, List2第二個數小於List1第二個數, List2第二個數大於List1第一個數
    # 重疊右邊: List2的第一個數大於List1第一個數, List2第一個數小於List1第二個數, List2第二個數大於List1第二個數
    # 合併方式: 
    #   包含在內: 用 List1 的 兩數
    #   重疊左邊: 用 List2 的小數, List1 的大數
    #   重疊右邊: 用 List1 的小數, List2 的大數

    # List1: input_list[i]
    # List2: input_list[j]

    while True:
        count = True
        for i in range(len(input_list)):
            for j in range(len(input_list)):
                if i == j:
                    continue
                # 包含在內
                elif input_list[j][0] >= input_list[i][0] and input_list[j][1] <= input_list[i][1]:
                    temp_list = []
                    temp_list.append([input_list[i][0], input_list[i][1]])
                    for couuu in range(len(input_list)):
                        if couuu != i and couuu != j:
                            temp_list.append(input_list[couuu])
                    input_list = temp_list
                    count = False
                    break
                # 重疊左邊
                elif input_list[j][0] <= input_list[i][0] and input_list[j][1] <= input_list[i][1] and input_list[j][1] >= input_list[i][0]:
                    temp_list = []
                    temp_list.append([input_list[j][0], input_list[i][1]])
                    for couuu in range(len(input_list)):
                        if couuu != i and couuu != j:
                            temp_list.append(input_list[couuu])
                    input_list = temp_list
                    count = False
                    break
                # 重疊右邊
                elif input_list[j][0] >= input_list[i][0] and input_list[j][0] <= input_list[i][1] and input_list[j][1] >= input_list[i][1]:
                    temp_list = []
                    temp_list.append([input_list[i][0], input_list[j][1]])
                    for couuu in range(len(input_list)):
                        if couuu != i and couuu != j:
                            temp_list.append(input_list[couuu])
                    input_list = temp_list
                    count = False
                    break
            
            if count == False:
                break
        if count == True:
            break

    result_num = 0
    for rum in input_list:
        result_num = result_num + (int(rum[1]) - int(rum[0]))
    print(result_num)
