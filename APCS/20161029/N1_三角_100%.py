# https://zerojudge.tw/ShowProblem?problemid=c294

while True:
    try:
        three_num = input()
    except:
        break
    num_list = three_num.split(" ")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    a, b, c = sorted(num_list)
    print(str(a) + " " + str(b) + " " + str(c))

    # 若 a、b、c 為三個線段的邊長，且 c 為最大值，則
    # 若 a+b ≦ c，三線段無法構成三角形
    # 若 a×a+b×b ＜ c×c，三線段構成鈍角三角形(Obtuse triangle)
    # 若 a×a+b×b ＝ c×c，三線段構成直角三角形(Right triangle)
    # 若 a×a+b×b ＞ c×c，三線段構成銳角三角形(Acute triangle)
    
    if a+b <= c:
        print("No")
    elif (a*a + b*b) < c*c:
        print("Obtuse")
    elif (a*a + b*b) == c*c:
        print("Right")
    elif (a*a + b*b) > c*c:
        print("Acute")
