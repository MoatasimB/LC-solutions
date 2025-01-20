class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last = {}

        for i in range(len(s)):
            last[s[i]] = i
        
        seen = set()
        stack = []

        for i in range(len(s)):
            if s[i] not in seen:
                while stack and stack[-1] >= s[i] and i < last[stack[-1]]:
                    x = stack.pop()
                    seen.remove(x)
                
                seen.add(s[i])
                stack.append(s[i])

        return "".join(stack)
                
