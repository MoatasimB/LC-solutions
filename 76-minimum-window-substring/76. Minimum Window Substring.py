class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq = defaultdict(int)

        for ch in t:
            freq[ch] += 1
        
        req = len(freq)

        l = 0
        length = float("inf")
        startIdx = -1
        for r in range(len(s)):
            ch = s[r]

            if ch in freq:
                freq[ch] -= 1
                if freq[ch] == 0:
                    req -= 1
            
            while req == 0:
                if r - l + 1 < length:
                    length = r - l + 1
                    startIdx = l
                
                ch = s[l]
                if ch in freq:
                    freq[ch] += 1
                    if freq[ch] - 1 == 0:
                        req += 1
                l += 1
        

        return s[startIdx: startIdx + length] if length != float("inf") else ""
