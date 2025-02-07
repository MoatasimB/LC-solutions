class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                curr_str = []
                while stack and stack[-1] != '[':
                    curr_str.append(stack.pop())
                stack.pop()
                x = 0
                y = len(curr_str) - 1
                while x < y:
                    curr_str[x], curr_str[y] = curr_str[y], curr_str[x]
                    x +=1
                    y -=1
                curr_str = "".join(curr_str)
                mul = 0
                count = 0
                while stack and stack[-1] in '0123456789':
                    num = int(stack.pop())
                    count += (10**mul)*num
                    mul +=1
                print(count)
                curr_str = curr_str * count
                stack.append(curr_str)
            else:
                stack.append(s[i])
        
        return "".join(stack)
            
