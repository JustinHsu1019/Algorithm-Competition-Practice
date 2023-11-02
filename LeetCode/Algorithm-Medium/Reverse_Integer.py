# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if str_x[0] == '-':
            if int('-' + str_x[1::][::-1]) > (2**31 - 1) or int('-' + str_x[1::][::-1]) < (-2)**31:
                return 0
            return int('-' + str_x[1::][::-1])
        elif int(str_x[::-1]) > (2**31 - 1) or int(str_x[::-1]) < (-2)**31:
            return 0
        else:
            return int(str_x[::-1])

def main():
    quest = 1534236469
    sol = Solution()
    result = sol.reverse(quest)
    print(result)

if __name__ == "__main__":
    main()