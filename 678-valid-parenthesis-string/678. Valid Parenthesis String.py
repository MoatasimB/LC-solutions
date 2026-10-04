class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # memo = {}
        # def dfs(i, count):
        #     if (i, count) in memo:
        #         return memo[(i, count)]
        #     if i == n:
        #         return count == 0
        #     if count < 0:
        #         return False
        #     ch = s[i]
        #     if ch == "(":
        #         if dfs(i + 1, count + 1):
        #             return True
        #     elif ch == ")":
        #         if dfs(i + 1, count - 1):
        #             return True
        #     else:
        #         if dfs(i + 1, count - 1) or dfs(i + 1, count + 1) or dfs(i + 1, count):
        #             return True
        #     memo[(i, count)] = False
        #     return False
        # return dfs(0,0)

        
        stack = []
        stars = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
        
        i = 0
        j = 0
        while i < len(stack) and j < len(stars):
            if stack[i] < stars[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(stack)
        
