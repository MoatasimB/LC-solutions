class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [["", -1]]
        ans = 0
        for i, ch in enumerate(s):
            if ch == "(":
                # ans = max(ans, i - stack[-1][1])
                stack.append(["(", i])
            else:
                if stack[-1][0] == "(":
                    stack.pop()
                    ans = max(ans, i - stack[-1][1])
                else:
                    stack.append([")", i])
        
        return ans

