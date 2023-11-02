# https://leetcode.com/problems/3sum

from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for k in range(len(nums)):
#             for j in range(len(nums)):
#                 for i in range(len(nums)):
#                     if i == j or i == k or j == k:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         temp = sorted([nums[i], nums[j], nums[k]])
#                         if temp not in result:
#                             result.append(temp)
#         return sorted(result)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1
        return result

def main():
    quest = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    ans = sol.threeSum(quest)
    print(ans)

if __name__ == "__main__":
    main()