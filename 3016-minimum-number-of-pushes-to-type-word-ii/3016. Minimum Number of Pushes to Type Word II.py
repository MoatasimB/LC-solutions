class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freq = defaultdict(int)

        for ch in word:
            freq[ch] += 1
        
        sorted_counts = sorted([[val, ch] for ch, val in freq.items()], reverse=True)

        #8 values
        ans = 0

        for i, x in enumerate(sorted_counts):
            count, ch = x

            mult = (i // 8) + 1
            ans += mult * count

        return ans
