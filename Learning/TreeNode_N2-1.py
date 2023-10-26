# https://www.youtube.com/watch?v=BkszA-MvjXA&t=323s&ab_channel=HackBear%E6%B3%B0%E7%91%9E

# 定義一個圖的數據結構。每個鍵都是一個節點，而值是該節點的相鄰節點
tree = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 5],
    4: [1, 6],
    5: [2, 3, 7, 8],
    6: [4, 7],
    7: [5, 6],
    8: [5]
}

# 函數返回給定鍵的相鄰節點
def get_neighbours(key):
    return tree[key]

def farthest_from_root(start):
    # 用於存儲已訪問過的節點的集合
    visited = set()
    # 使用列表作為隊列來存儲要訪問的節點和它們到起始節點的距離
    queue = [(start, 0)]
    # 將起始節點添加到已訪問的集合中
    visited.add(start)
    current_node, distance = None, None

    while queue:
        # 從隊列的前端取出一個節點和它的距離
        current_node, distance = queue.pop(0)

        for neighbour in get_neighbours(current_node):
            if neighbour not in visited:
                # 將鄰居和它到起始節點的距離加1添加到隊列中
                queue.append((neighbour, distance + 1))
                visited.add(neighbour)

    return current_node, distance

longest_dis = 0
for i in range(1, 9):
    node, distance = farthest_from_root(i)
    if distance > longest_dis:
        longest_dis = distance

print(longest_dis)

# 使用廣度優先搜索（BFS）來搜索圖
def search_graph(start):
    # 用於存儲搜索結果的字符串
    result = ""
    # 用集合存儲已經訪問過的節點
    visited = set()
    # 使用列表作為隊列來存儲要訪問的節點
    queue = [start]
    # 將起始節點添加到已訪問的集合中
    visited.add(start)

    # 當隊列不為空時繼續搜索
    while queue:
        # 從隊列的前端取出一個節點
        current_node = queue.pop(0)
        # 將當前節點添加到結果字符串中
        result = result + str(current_node) + ", "
        
        # 對當前節點的每個相鄰節點進行迭代
        for neighbour in get_neighbours(current_node):
            # 如果相鄰節點還沒有被訪問過
            if neighbour not in visited:
                # 將它添加到隊列和已訪問集合中
                queue.append(neighbour)
                visited.add(neighbour)

    # 打印結果字符串，但去掉末尾的逗號和空格
    print(result[0:-2])

# 從節點1開始搜索圖
search_graph(1)
