# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ""
        current_count = 0
        for i in range(len(s)):
            strin = s[i::]
            for j in range(1, len(strin)+1):
                if strin[:j:] == strin[:j:][::-1] and len(strin[:j:]) > current_count:
                    longest_str = strin[:j:]
                    current_count = len(longest_str)
        return longest_str

def main():
    s = "bbab"
    sol = Solution()
    longest = sol.longestPalindrome(s)
    print(longest)

if __name__ == "__main__":
    main()
