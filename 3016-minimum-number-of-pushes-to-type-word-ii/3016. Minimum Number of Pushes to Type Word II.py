class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freq = Counter(word)

        ans = 0

        for i, count in enumerate(sorted(freq.values(), reverse=True)):
            mult = (i // 8) + 1
            ans += mult * count

        return ans
