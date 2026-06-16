class Solution:
    def processStr(self, s: str) -> str:
        
        n = len(s)

        stack = []

        for i in range(n):
            if s[i] == "*":
                if stack:
                    stack.pop()
            elif s[i] == "#":
                stack_len = len(stack)
                for i in range(stack_len):
                    stack.append(stack[i])
            elif s[i] =="%":
                i = 0
                j = len(stack) - 1
                while i < j:
                    stack[i], stack[j] = stack[j], stack[i]
                    i += 1
                    j -= 1
                
            else:
                stack.append(s[i])
        
        return "".join(stack)