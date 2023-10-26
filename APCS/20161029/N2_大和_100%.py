# https://zerojudge.tw/ShowProblem?problemid=c295

while True:
    try:
        N, M = input().split(" ")
    except:
        break
    N = int(N)
    M = int(M)
    big_list = []
    all_num = []
    count = 0
    for i in range(N):
        temp = input().split(" ")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        big_list.append(sorted(temp))
        count += int(big_list[i][-1])
    print(count)
    for i in range(N):
        if count % int(big_list[i][-1]) == 0:
            all_num.append(int(big_list[i][-1]))
    if all_num == []:
        print(-1)
    else:
        ans = ""
        for result in all_num:
            ans =  ans + str(result) + " " 
        print(ans[0:-1])
