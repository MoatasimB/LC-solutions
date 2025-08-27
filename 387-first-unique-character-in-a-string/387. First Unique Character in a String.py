class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        indices = {s[i] : i for i in range(len(s))} # ch : idx

        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        
        ans = float('inf')

        for ch, count in counts.items():
            if count == 1:
                ans = min(ans, indices[ch])
        
        return ans if ans != float('inf') else -1