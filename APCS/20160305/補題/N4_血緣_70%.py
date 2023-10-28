# https://zerojudge.tw/ShowProblem?problemid=b967

from collections import deque

def bfs(tree, start):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    current_distance = None
    current_node = None
    
    while queue:
        current_node, current_distance = queue.popleft()

        for child in tree[current_node]:
            if child not in visited:
                queue.append((child, current_distance+1))
                visited.add(child)
    return current_distance, current_node

while True:
    try:
        how_many = int(input())
    except EOFError:
        break
    tree = {}
    for i in range(how_many):
        tree[i] = set()
    for _ in range(how_many - 1):
        a1, a2 = map(int, input().split(" "))
        tree[a1].add(a2)
        tree[a2].add(a1)

    _, node = bfs(tree, how_many-1)
    distance, _ = bfs(tree, node)
    print(distance)
