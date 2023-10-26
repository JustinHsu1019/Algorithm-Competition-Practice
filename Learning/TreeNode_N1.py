# 用 遞迴 遍歷 tree 並印出
def print_tree(tree, node, level=0):
    print(" " * level + node)

    if node in tree:
        for child in tree[node]:
            print_tree(tree, child, level+1)

# 用 DFS 遍歷 tree 並印出
def dfs_print_tree(tree, root):
    stack = [(root, 0)]

    while stack:
        node, level = stack.pop()
        print(" " * level + node)
        
        if node in tree:
            children = sorted(tree[node], reverse=True)
            for child in children:
                stack.append((child, level+1))

while True:
    # 輸入內容
    try:
        members = int(input())
    except:
        break

    # 處理輸入並寫入 tree 中
    tree = {}
    all_child = set()
    for i in range(members):
        parent, child = input().split(" ")
        tree.setdefault(parent, [])
        tree[parent].append(child)
        all_child.add(child)

    # 找出樹的根節點
    ancestor = None
    for parent in tree:
        if parent not in all_child:
            ancestor = parent

    # 遞迴
    print_tree(tree, ancestor)
    # DFS
    dfs_print_tree(tree, ancestor)
