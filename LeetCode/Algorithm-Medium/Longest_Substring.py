# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_count = 0
        for i in range(len(s)):
            visited = set()
            count = 0
            strin = s[i::]
            for j in range(len(strin)):
                if strin[j] not in visited:
                    visited.add(strin[j])
                    count += 1
                else:
                    break
            if count > longest_count:
                longest_count = count
        return longest_count

def main():
    s = "pwwkew"
    sol = Solution()
    longest = sol.lengthOfLongestSubstring(s)
    print(longest)

if __name__ == "__main__":
    main()
