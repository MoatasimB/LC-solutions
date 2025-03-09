class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
                continue
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    stack.append(ch)
        
        return len(stack)