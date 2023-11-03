# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass

def main():
    # Create a linked list: l1 = 2 -> 4 -> 9
    l1 = ListNode(2, ListNode(4, ListNode(9)))

    sol = Solution()
    ans = sol.removeNthFromEnd(l1)

if __name__ == "__main__":
    main()
