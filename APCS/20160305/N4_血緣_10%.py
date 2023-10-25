# https://zerojudge.tw/ShowProblem?problemid=b967

while True:
    try:
        how_many = int(input())
    except:
        break
    big_list = []
    count_li = []
    for i in range(how_many):
        count_li.append(0)
    for i in range(how_many-1):
        tempstr = input()
        temp = tempstr.split(" ")
        count_li[int(temp[1])] += 1
        big_list.append(temp)

    the_one = 0
    for i in range(len(count_li)):
        if count_li[i] == 0:
            the_one = i
            break
  
    count = 0
    for i in range(how_many-1):
        if big_list[i][0] == str(the_one):
            count += 1

    if count == 1:
        print(how_many-1)
    elif count == 2:
        print(how_many-1)
    else:
        print(how_many-2)
