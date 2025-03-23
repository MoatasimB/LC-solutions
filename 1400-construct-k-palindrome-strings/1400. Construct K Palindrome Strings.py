class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k :
            return False

        counts = defaultdict(int)

        for ch in s:
            counts[ch] += 1
        

        oddCount = 0
        for val in counts.values():
            oddCount += 1 if val % 2 != 0 else 0

        return oddCount <= k