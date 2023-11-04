# https://www.youtube.com/watch?v=BkszA-MvjXA&t=323s&ab_channel=HackBear%E6%B3%B0%E7%91%9E

# 使用 collections deque popleft() --> O(1)
# 使用 Python List pop(0) --> O(n)
from collections import deque

tree = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 5],
    4: [1, 6],
    5: [2, 3, 7],
    6: [4, 7],
    7: [5, 6]
}

def get_neighbours(key):
    return tree.get(key, [])

def search_graph(start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(str(current_node))
        for neighbour in get_neighbours(current_node):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

    return ', '.join(result)

print(search_graph(1))
