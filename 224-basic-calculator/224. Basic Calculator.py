class Solution:
    def calculate(self, s: str) -> int:
        
        sign = 1
        num = 0
        res = 0
        stack = []
        i=0
        while i < len(s):

            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            elif s[i] in "-+":
                res += num * sign
                if s[i] == "+":
                    sign = 1
                else:
                    sign = -1
                num = 0
            
            elif s[i] == "(":
                stack.append(res)
                stack.append(sign)

                num = 0
                sign = 1
                res = 0
            
            elif s[i] == ")":
                res += num * sign
                sign = stack.pop()
                num = stack.pop()
                res *= sign
                res += num

                num = 0
                sign = 1
            
            i+=1
        
        return res + num*sign
