class Solution:
    def decodeString(self, s: str) -> str:
        
        num_stack = []
        str_stack = []

        curr = ""
        num = 0

        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                num_stack.append(num)
                str_stack.append(curr)
                num = 0
                curr = ""
            elif s[i] == "]":
                mult = num_stack.pop()
                tmp = mult * curr
                curr = str_stack.pop()
                curr += tmp

                num = 0
            else:
                curr += s[i]
        
        return curr