# https://zerojudge.tw/ShowProblem?problemid=c296

while True:
    try:
        N, M, K = input().split(" ")
    except:
        break
    N = int(N)
    M = int(M)
    K = int(K)
    big_list = []
    for i in range(N):
        big_list.append("")
    for i in range(1, N+1):
        if i == 1:
            big_list[i-1] = str(i) + ":True"
        else:
            big_list[i-1] = str(i) + ":False"
    newb = None
    for _ in range(K):
        boom_index = None
        boom_human = None
        for i in range(len(big_list)):
            what  = big_list[i].split(":")
            if what[-1] == "True":
                boom_index = i
                boom_human = what[0]
                big_list[boom_index] = str(boom_human) + ":False"
        newb = str((big_list[(boom_index+(M-1)+1)%len(big_list)].split(":"))[0])
        big_list[(boom_index+(M-1)+1)%len(big_list)] = newb + ":True"
        big_list.remove(big_list[(boom_index+(M-1))%len(big_list)])
    print(newb)
