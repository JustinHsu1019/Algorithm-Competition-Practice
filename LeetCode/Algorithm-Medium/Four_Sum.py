# https://leetcode.com/problems/4sum

# 未完成

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            for i in range(len(nums)):
                if i == j:
                    continue
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    sum_ = nums[j] + nums[i] + nums[left] + nums[right]
                    if sum_ == target:
                        if j != left and j != right:
                            temp = sorted([nums[j], nums[i], nums[left], nums[right]])
                            if temp not in result:
                                result.append(temp)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        right -= 1
        return result

def main():
    quest = [2,2,2,2,2]
    target = 8
    sol = Solution()
    ans = sol.fourSum(quest, target)
    print(ans)

if __name__ == "__main__":
    main()
