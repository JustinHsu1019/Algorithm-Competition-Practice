# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, findFirst=True):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid
                    if findFirst:
                        right = mid - 1 
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        if not nums:
            return [-1, -1]

        firstPos = binarySearch(nums, target, True)
        if firstPos == -1:
            return [-1, -1]

        lastPos = binarySearch(nums, target, False)

        return [firstPos, lastPos]

def main():
    quest = [5,7,7,8,8,10]
    target = 8
    sol = Solution()
    ans = sol.searchRange(quest, target)
    print(ans)

if __name__ == "__main__":
    main()
