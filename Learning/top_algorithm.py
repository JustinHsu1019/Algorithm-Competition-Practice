# Default Settings
tree = {
	"1": ["2","3","4"],
	"2": ["5","6"],
	"3": ["7"],
	"4": ["8"],
	"5": [],
	"6": [],
	"7": [],
	"8": []
}
array = [1, 3, 2, 7, 6, 5]

class TreeNode:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# BFS
def get_allB(root):
	result = []
	visited = set()
	queue = [root]

	while queue != []:
		currend_node = queue.pop(0)
		visited.add(currend_node)
		result.append(currend_node)

		for naber in tree[currend_node]:
			if naber not in visited:
				queue.append(naber)

	return result

# DFS
def get_allD(root):
	result = []
	visited = set()
	stack = [root]

	while stack != []:
		current_node = stack.pop()
		visited.add(current_node)
		result.append(current_node)

		for neighbor in reversed(tree[current_node]):
			if neighbor not in visited:
				stack.append(neighbor)

	return result

# Binary tree basic
def binaryt():
	# 第四層
	node8 = TreeNode(8)
	node9 = TreeNode(9)
	node10 = TreeNode(10)
	node11 = TreeNode(11)
	node12 = TreeNode(12)
	node13 = TreeNode(13)
	node14 = TreeNode(14)
	node15 = TreeNode(15)

	# 第三層
	node4 = TreeNode(4, node8, node9)
	node5 = TreeNode(5, node10, node11)
	node6 = TreeNode(6, node12, node13)
	node7 = TreeNode(7, node14, node15)

	# 第二層
	node2 = TreeNode(2, node4, node5)
	node3 = TreeNode(3, node6, node7)

	# 根節點
	node1 = TreeNode(1, node2, node3)

	return node1

# Binary tree advanced
def list_to_tree(lst):
	nodes = []  # 初始化一個空列表來存儲所有節點
	for val in lst:  # 遍歷給定的列表
		if val is None:
			nodes.append(None)  # 如果值是None，則添加None到節點列表中
		else:
			nodes.append(TreeNode(val))  # 否則，創建一個新的TreeNode並添加到列表中

	kids = nodes[::-1]  # 反轉節點列表，準備從後向前分配子節點
	root = kids.pop()  # 彈出最後一個元素作為根節點
	for node in nodes:
		if node:  # 如果節點不是None
			# 分配左子節點
			if len(kids) > 0:  # 如果kids列表不為空
				node.left = kids.pop()  # 從kids列表的末尾彈出一個節點並設置為當前節點的左子節點
			else:
				node.left = None  # 如果kids列表為空，則設置當前節點的左子節點為None

			# 分配右子節點
			if len(kids) > 0:  # 如果kids列表不為空
				node.right = kids.pop()  # 從kids列表的末尾彈出一個節點並設置為當前節點的右子節點
			else:
				node.right = None  # 如果kids列表為空，則設置當前節點的右子節點為None

	return root

# search binary tree
def search_binary_tree(root, target):
	if root is None:
		return None
	if root.val == target:
		return root
	left_search = search_binary_tree(root.left, target)
	if left_search:
		return left_search
	right_search = search_binary_tree(root.right, target)
	return right_search

# Linear search (Original list)
def linears(target):
	for i, re in enumerate(array):
		if re == target:
			return i

# Binary search (Original list)
def binary_search(arrr, target):
	arr = sorted(arrr)
	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1

# Linked List
class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, key):
		new_node = Node(key)
		if self.head == None:
			self.head = new_node
			return
		current = self.head
		while current.next:
			current = current.next

		current.next = new_node
		return

	def display(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
		print("None")
		return

	def delete(self, key):
		current = self.head
		if current and key == current.data:
			self.head = current.next
			return

		prev = None
		while current and current.data != key:
			prev = current
			current = current.next

		if current == None:
			return

		prev.next = current.next
		return

# main
if __name__ == "__main__":
	# BFS
	print(get_allB("1"))

	# DFS
	print(get_allD("1"))

	# binary tree basic
	print(binaryt())

	# binary tree advanced
	root, target = list_to_tree(array), 3
	print(search_binary_tree(root, target))

	# linear search
	print(linears(2))

	# binary search
	index = binary_search(array, 3)
	if index != -1:
		print(f"Found target 3 at index {index}.")
	else:
		print(f"Target 3 not found in the array.")

	# linked list playground
	llist = LinkedList()
	llist.append(1)
	llist.append(2)
	llist.append(3)
	print("原始鏈表:")
	llist.display()

	llist.delete(1)
	print("刪除節點後的鏈表:")
	llist.display()
