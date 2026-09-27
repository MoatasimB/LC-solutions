class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == ")":
                curr = []
                while stack:
                    val = stack.pop()
                    if val == "(":
                        break
                    curr.append(val)
                stack.extend(curr)
                curr = []
            else:
                stack.append(s[i])
        
        return "".join(stack)
        
        
        # i = 0
        # def dfs(): #return reversed string
        #     nonlocal i
        #     curr = []
        #     if s[i] == ")"

