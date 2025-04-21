class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        app = {ch: [float('inf'),0] for ch in s}
        ans = 0
        for i in range(len(s)):
            app[s[i]][0] = min(app[s[i]][0], i)
            app[s[i]][1] = i

        print(app)
        
        for ch in app:
            beg = app[ch][0]
            used = set()
            for i in range(beg + 1, app[ch][1]):
                used.add(s[i])
            ans += len(used)
        
        return ans
        