class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        ans = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                    ans = max(ans, i - stack[-1] if stack else i + 1)
                else:
                    stack.append(i)
        
        return ans

