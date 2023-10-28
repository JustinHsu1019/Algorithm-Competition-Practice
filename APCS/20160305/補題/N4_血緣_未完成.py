# https://zerojudge.tw/ShowProblem?problemid=b967

def bfs(tree, start):
    visited = set()
    queue = [(start, 0)]
    visited.add(start)
    current_distance = None
    current_node = None
    
    while queue:
        current_node, current_distance = queue.pop(0)

        for child in tree[current_node]:
            if child not in visited:
                queue.append((child, current_distance+1))
                visited.add(child)
    return current_distance, current_node

while True:
    try:
        how_many = int(input())
    except:
        break
    tree = {}
    for i in range(how_many):
        tree[i] = set()
    for _ in range(how_many - 1):
        a1, a2 = map(int, input().split(" "))
        tree[a1].add(a2)
        tree[a2].add(a1)

    distance01, node = bfs(tree, 0)
    distance02, _ = bfs(tree, node)
    print(distance01 + distance02)
