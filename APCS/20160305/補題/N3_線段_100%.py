while True:
    try:
        N = int(input())
    except EOFError:
        break

    segments = []
    for _ in range(N):
        L, R = map(int, input().split())
        segments.append((L, R))

    segments.sort()

    covered_length = 0
    current_start, current_end = segments[0]

    for i in range(1, N):
        if segments[i][0] <= current_end:
            current_end = max(current_end, segments[i][1])
        else:
            covered_length += current_end - current_start
            current_start, current_end = segments[i]

    covered_length += current_end - current_start

    print(covered_length)
