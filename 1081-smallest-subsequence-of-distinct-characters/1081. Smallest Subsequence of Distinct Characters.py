class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        lastOcc = {}
        for i in range(len(s)):
            lastOcc[s[i]] = i
        
        stack = []
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                while stack and stack[-1] > s[i] and i < lastOcc[stack[-1]]:
                    x = stack.pop()
                    seen.remove(x)
                
                seen.add(s[i])
                stack.append(s[i])
        
        return "".join(stack)