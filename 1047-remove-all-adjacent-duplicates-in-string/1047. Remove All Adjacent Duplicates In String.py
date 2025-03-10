class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):

            if stack and stack[-1] == s[i]:
                stack.pop()
                continue
            stack.append(s[i])
        
        return "".join(stack)