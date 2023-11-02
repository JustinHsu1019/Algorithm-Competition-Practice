# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        return_str = ""
        check = 0
        visited = []
        for i in range(len(s)):
            if s[i] in ["0","1","2","3","4","5","6","7","8","9","-", " ", ".", "+"]:
                if i == "-":
                    if i+2 < len(s):
                        if s[i+1] in ["0","1","2","3","4","5","6","7","8","9"]:
                            if check == 0 and i != 0:
                                return 0
                            else:
                                check = 1
                            return_str += s[i]
                            visited.append(i)
                else:
                    if check == 0 and i != 0:
                        return 0
                    else:
                        check = 1
                    return_str += s[i]
                    visited.append(i)
        try:
            if return_str[-1] == "-":
                return_str = return_str[:len(return_str)-1:]
        except:
            return 0
        for i in range(len(visited)):
            if i != (len(visited)-1):
                if visited[i+1] != visited[i] + 1:
                    return_str = return_str[:i+1:]
        list_re = return_str.split(" ")
        temp = []
        for i in list_re:
            if i != '':
                temp.append(i)
        try:
            return_str = temp[0]
        except:
            return 0
        if "+" in return_str:
            temp = return_str.replace(" ", "")
            if temp[0] == "+":
                try:
                    if return_str[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                        return_str = return_str.replace("+", "")
                except:
                    return 0
            else:
                for i in range(len(return_str)):
                    if return_str[i] == "+":
                        return_str = return_str[:i:]
                        break
        if "." in return_str:
            return_str = str(int(float(return_str)))
        try:
            if "-" in return_str and return_str.replace(" ","")[0] != "-":
                for i in range(len(return_str)):
                    if return_str[i] == "-":
                        return_str = return_str[:i:]
                        break
        except:
            _ = 0
        try:
            if int(return_str) > 2**31 - 1:
                return 2**31 -1
            elif int(return_str) < (-2)**31:
                return (-2)**31
            return int(return_str)
        except:
            return 0

def main():
    quest = "3-5"
    sol = Solution()
    result = sol.myAtoi(quest)
    print(result)

if __name__ == "__main__":
    main()