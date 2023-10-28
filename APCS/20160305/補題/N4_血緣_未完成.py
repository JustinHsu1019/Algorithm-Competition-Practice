# https://zerojudge.tw/ShowProblem?problemid=b967

from collections import deque

def bfs(tree, start):
    visited = [False] * len(tree)
    queue = deque([(start, 0)])
    visited[start] = True
    current_distance = None
    current_node = None

    while queue:
        current_node, current_distance = queue.popleft()

        for child in tree[current_node]:
            if not visited[child]:
                queue.append((child, current_distance+1))
                visited[child] = True
    return current_distance, current_node

while True:
    try:
        how_many = int(input())
    except EOFError:
        break

    tree = [[] for _ in range(how_many)]
    for _ in range(how_many - 1):
        a1, a2 = map(int, input().split())
        tree[a1].append(a2)
        tree[a2].append(a1)

    leaf_node = next(i for i, neighbors in enumerate(tree) if len(neighbors) == 1)
    _, node = bfs(tree, leaf_node)
    distance, _ = bfs(tree, node)
    print(distance)
