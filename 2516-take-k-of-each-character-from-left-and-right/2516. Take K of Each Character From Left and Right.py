class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        freq = defaultdict(int)
        n = len(s)
        for ch in s:
            freq[ch] += 1
        for ch in "abc":
            if ch not in freq or freq[ch] < k:
                return -1
        ans = float("inf")
        l = 0
        for r in range(len(s)):
            freq[s[r]] -= 1
            #while outside freq of chs is less than k
            while freq[s[r]] < k:
                freq[s[l]] += 1
                l += 1
            
            ans = min(ans, l + (n - r - 1))

        return ans if ans != float("inf") else -1