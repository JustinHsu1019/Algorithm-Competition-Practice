# https://leetcode.com/problems/swap-nodes-in-pairs

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        head_list = []
        while current:
            head_list.append(current.val)
            current = current.next

        if not head_list:
            return None

        count = len(head_list) // 2

        for i in range(count):
            temp = head_list[i * 2]
            head_list[i * 2] = head_list[i * 2 + 1]
            head_list[i * 2 + 1] = temp

        dummy = ListNode(head_list[0])
        current = dummy

        for i in range(1, len(head_list)):
            current.next = ListNode(head_list[i])
            current = current.next

        return dummy

def main():
    # Create a linked list: head = 2 -> 4 -> 9
    head = ListNode(2, ListNode(4, ListNode(9)))

    sol = Solution()
    ans = sol.swapPairs(head)

    current = ans
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

if __name__ == "__main__":
    main()
