class Solution:
    def decodeString(self, s: str) -> str:
        
        str_stack = []
        num_stack = []


        num = 0
        curr = ""

        for i in range(len(s)):
            if s[i].isdigit():
                num = (num * 10) + int(s[i])
            elif s[i] == "[":
                str_stack.append(curr)
                num_stack.append(num)
                curr = ""
                num = 0
            elif s[i] == "]":
                subStr = str_stack.pop()
                mult = num_stack.pop()
                curr = mult * curr
                subStr += curr
                curr = subStr
                num = 0
            else:
                curr += s[i]

        return curr


