# https://leetcode.com/problems/3sum-closest

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        current_close = None
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while right > left:
                current = nums[i] + nums[left] + nums[right]
                if current_close == None:
                    current_close = current
                elif abs(current-target) < abs(current_close-target):
                    current_close = current
                if current-target > 0:
                    right -= 1
                else:
                    left += 1
        return current_close

def main():
    quest = [-1,2,1,-4]
    target = 1
    sol = Solution()
    ans = sol.threeSumClosest(quest, target)
    print(ans)

if __name__ == "__main__":
    main()