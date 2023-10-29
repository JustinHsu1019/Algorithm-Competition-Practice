# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        current = l1
        while current:
            num1 += str(current.val)
            current = current.next
        current = l2
        while current:
            num2 += str(current.val)
            current = current.next
        print(num1)
        print(num2)
        
def main():
    # Create two linked lists: l1 = 2 -> 4 -> 3 and l2 = 5 -> 6 -> 4
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    s = Solution()
    s.addTwoNumbers(l1, l2)

if __name__ == "__main__":
    main()
