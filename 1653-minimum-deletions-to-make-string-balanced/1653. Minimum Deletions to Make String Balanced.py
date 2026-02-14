class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        ans = 0
        freq_b = 0

        for ch in s:
            if ch == 'a' and freq_b > 0:
                ans += 1
                freq_b -= 1
            elif ch == 'a':
                continue
            else:
                freq_b += 1

        return ans