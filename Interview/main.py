# https://app.coderpad.io/Q9TQ22H3

# From Terry Channel
# https://www.youtube.com/watch?v=BkszA-MvjXA&t=323s&ab_channel=HackBear%E6%B3%B0%E7%91%9E

import requests

apiEndpoint = "https://justinhsu.pythonanywhere.com/TreeNode/get_neighbours?key="

def fetchNeighbours(node):
    try:
        response = requests.get(apiEndpoint + str(node), timeout=10)

        if response.status_code == 200:
            return response.json().get('neighbours', [])
        else:
            print(response.json().get('error'))
            return []
    except Exception as error:
        print("Error: " + str(error))
        return []

# 1 -> [2, 3, 4]
# 2 -> [1, 5]
# 3 -> [1, 5]
# 4 -> [1, 6]
# 5 -> [2, 3, 7, 8]
# 6 -> [4, 7]
# 7 -> [5, 6]
# 8 -> [5]
# print: 1, 2, 3, 4, 5, 6, 7, 8
# Also this is valid: 1, 4, 3, 2, 6, 5, 7, 8

# You will be working on this part
def searchGraph(start):
    neighbours = fetchNeighbours(start)
    print(str(neighbours)[1:-1])

searchGraph(1)
