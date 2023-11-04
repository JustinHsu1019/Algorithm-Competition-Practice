# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        head_list = []
        while current:
            head_list.append(current.val)
            current = current.next
        head_list.pop(-1*n)

        if not head_list:
            return None

        dummy = ListNode(head_list[0])
        current = dummy

        for i in range(1, len(head_list)):
            current.next = ListNode(head_list[i])
            current = current.next

        return dummy

def main():
    # Create a linked list: head = 2 -> 4 -> 9
    head = ListNode(2, ListNode(4, ListNode(9)))
    n = 1

    sol = Solution()
    ans = sol.removeNthFromEnd(head, n)

    current = ans
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

if __name__ == "__main__":
    main()
