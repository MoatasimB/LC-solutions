class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        
        stack = []
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:

                while stack and stack[-1] >= s[i] and last[stack[-1]] > i:
                    x = stack.pop()
                    seen.remove(x)
                
                stack.append(s[i])
                seen.add(s[i])
            print(seen)
        return "".join(stack)