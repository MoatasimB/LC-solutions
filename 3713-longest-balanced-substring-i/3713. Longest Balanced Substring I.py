class Solution:
    def longestBalanced(self, s: str) -> int:
        
        ans = 0
        for l in range(len(s)):
            freq = defaultdict(int)
            for r in range(l, len(s)):
                freq[s[r]] += 1
                if len(set(list(freq.values()))) == 1 and r - l + 1 > ans:
                    ans = max(ans, r - l + 1)
        
        return ans


