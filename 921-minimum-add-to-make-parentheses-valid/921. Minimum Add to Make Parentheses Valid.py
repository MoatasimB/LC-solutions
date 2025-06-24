class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        pair = ["(", ")"]

        stack = []

        for i in range(len(s)):
            if s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                
            stack.append(s[i])
        
        return len(stack)
