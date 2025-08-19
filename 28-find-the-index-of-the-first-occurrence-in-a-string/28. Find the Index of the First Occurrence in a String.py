class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(haystack)
        m = len(needle)
        p = 31
        MOD = 10**9 + 7

        max_factor = 1

        for _ in range(m):
            max_factor = (max_factor * p) % MOD
        def hash(word):

            ans = 0
            mult = 1
            for i in range(m - 1, -1, -1):
                ans += ((ord(word[i]) - ord('a')) * mult) % MOD
                mult = (mult * p) % MOD
            
            return ans % MOD
        

        needle_hash = hash(needle)

        for i in range(n - m + 1):
            if i == 0:
                hay_hash = hash(haystack)
            else:
                hay_hash = (((hay_hash * p) % MOD) - (((ord(haystack[i - 1]) - ord('a')) * max_factor)% MOD) + (ord(haystack[i + m - 1]) - ord('a'))) % MOD
            

            if hay_hash == needle_hash:
                for j in range(m):
                    if haystack[i + j] != needle[j]:
                        break
                if j == m - 1:
                    return i
        
        return -1
                
