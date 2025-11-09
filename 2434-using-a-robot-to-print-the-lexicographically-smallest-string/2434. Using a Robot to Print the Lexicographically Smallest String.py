class Solution:
    def robotWithString(self, s: str) -> str:
        
        stack = []

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        def find_smallest():
            for i in range(26):
                if freq[i] >= 1:
                    return i
            return 26
        t = []
        for i in range(len(s)):
            ch = s[i]
            freq[ord(ch) - ord('a')] -= 1
            stack.append(ch)

            while stack and ((ord(stack[-1]) - ord('a')) <= find_smallest()):
                t.append(stack.pop())
            
        
        while stack:
            t.append(stack.pop())
        
        return "".join(t)
