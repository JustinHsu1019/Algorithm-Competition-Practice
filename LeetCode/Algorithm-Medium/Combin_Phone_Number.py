# https://leetcode.com/problems/letter-combinations-of-a-phone-number

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 如果輸入的字符串為空，則返回空列表
        if not digits:
            return []

        # 電話號碼和字母的映射關係
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # 回溯函數來生成所有可能的字母組合
        def backtrack(index: int, path: str):
            # 如果當前的路徑長度和數字字符串長度相等，添加到結果中
            if index == len(digits):
                combinations.append(path)
                return
            
            # 獲取當前數字對應的所有可能字母
            possible_letters = phone_map[digits[index]]
            # 遍歷這些字母，進行回溯
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        # 用於存儲結果的列表
        combinations = []
        # 從第一個數字開始回溯
        backtrack(0, "")

        return combinations

def main():
    quest = "234"
    sol = Solution()
    ans = sol.letterCombinations(quest)
    print(ans)

if __name__ == "__main__":
    main()
