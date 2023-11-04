# https://leetcode.com/problems/next-permutation

# 進行中

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 僅考慮 len(nums) = 3, 練習 in-place 概念 (?)
        sort_nums = sorted(nums)
        nums_temp = sort_nums
        if sort_nums == nums:
            nums[0], nums[1], nums[2] = nums_temp[0], nums_temp[2], nums_temp[1]
        else:
            sort_nums = [nums_temp[0], nums_temp[2], nums_temp[1]]
            if sort_nums == nums:
                nums[0], nums[1], nums[2] = nums_temp[1], nums_temp[0], nums_temp[2]
            else:
                sort_nums = [nums_temp[1], nums_temp[0], nums_temp[2]]
                if sort_nums == nums:
                    nums[0], nums[1], nums[2] = nums_temp[1], nums_temp[2], nums_temp[0]
                else:
                    sort_nums = [nums_temp[1], nums_temp[2], nums_temp[0]]
                    if sort_nums == nums:
                        nums[0], nums[1], nums[2] = nums_temp[2], nums_temp[0], nums_temp[1]
                    else:
                        sort_nums = [nums_temp[2], nums_temp[0], nums_temp[1]]
                        if sort_nums == nums:
                            nums[0], nums[1], nums[2] = nums_temp[2], nums_temp[1], nums_temp[0]
                        else:
                            nums[0], nums[1], nums[2] = nums_temp[0], nums_temp[1], nums_temp[2]

        # 提交時無須 return, 此處僅供測試使用
        return nums

def main():
    quest = [3, 1, 2]
    sol = Solution()
    sorted_ = sol.nextPermutation(quest)
    print(sorted_)

if __name__ == "__main__":
    main()
