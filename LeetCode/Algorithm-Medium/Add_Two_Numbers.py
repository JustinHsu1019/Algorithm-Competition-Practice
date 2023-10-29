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
        
        total = str(int(num1[::-1]) + int(num2[::-1]))[::-1]

        firstone = ListNode(total[0])
        current = firstone

        for i in total[1::]:
            current.next = ListNode(int(i))
            current = current.next

        return firstone
        
def main():
    # Create two linked lists: l1 = 2 -> 4 -> 9 and l2 = 5 -> 6 -> 4 -> 9
    l1 = ListNode(2, ListNode(4, ListNode(9)))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))

    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    result = []
    current = l3
    while current:
        result.append(str(current.val))
        current = current.next
    print(result)

if __name__ == "__main__":
    main()
