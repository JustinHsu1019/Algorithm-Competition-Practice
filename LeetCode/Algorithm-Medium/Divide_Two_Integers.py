# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_ = 1
        if dividend // divisor < 0:
            min_ = -1
        ans = min_ * (abs(dividend) // abs(divisor))
        if ans > 2**31 -1:
            return 2**31 -1
        elif ans < -2**31:
            return -2**31
        return ans

def main():
    dividend = 7
    divisor = -3
    sol = Solution()
    ans = sol.divide(dividend, divisor)
    print(ans)

if __name__ == "__main__":
    main()
