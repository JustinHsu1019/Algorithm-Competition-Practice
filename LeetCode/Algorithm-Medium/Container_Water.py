# https://leetcode.com/problems/container-with-most-water

from typing import List

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         biggest = 0
#         for i in range(len(height)):
#             for j in range(len(height)):
#                 if i == j:
#                     continue
#                 current = abs(j-i)*(min(height[i], height[j]))
#                 if current > biggest:
#                     biggest = current
#         return biggest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggest = 0
        left = 0
        right = len(height) - 1

        while right != left:
            current = (right-left)*(min(height[left], height[right]))
            biggest = max(current, biggest)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return biggest

def main():
    quest = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    maxed = sol.maxArea(quest)
    print(maxed)

if __name__ == "__main__":
    main()