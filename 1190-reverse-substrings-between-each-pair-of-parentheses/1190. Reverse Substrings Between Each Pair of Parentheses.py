class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        # stack = []
        # n = len(s)
        # for i in range(n):
        #     if s[i] == ")":
        #         curr = []
        #         while stack:
        #             val = stack.pop()
        #             if val == "(":
        #                 break
        #             curr.append(val)
        #         stack.extend(curr)
        #         curr = []
        #     else:
        #         stack.append(s[i])
        
        # return "".join(stack)
        
        
        i = 0
        n = len(s)
        def dfs(): #return reversed string
            nonlocal i
            curr = []
            while i < n:
                if s[i] == ")":
                    i += 1
                    return reversed(curr)
                elif s[i] == "(":
                    i += 1
                    curr.extend(dfs())
                else:
                    curr.append(s[i])
                    i += 1
            return curr
 
        return "".join(dfs())


