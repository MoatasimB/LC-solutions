class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        p = 31
        MOD = 10**9 + 7
        m = len(haystack)
        n = len(needle)

        def hash(word):

            mult = 1
            h = 0
            for i in range(n - 1, -1, -1):
                h  += ((ord(word[i]) - ord('a')) * mult) % MOD
                mult = (mult * p) % MOD
            
            return h % MOD
        
        max_mult = 1

        for _ in range(n):
            max_mult =( max_mult * p) % MOD
        
        needle_hash = hash(needle)

        for i in range(m - n + 1):
            if i == 0:
                hay_hash = hash(haystack)
            else:
                hay_hash = (((hay_hash * p) % MOD) + ((ord(haystack[i + n - 1]) - ord('a')) % MOD) - (((ord(haystack[i - 1]) - ord('a')) * max_mult) % MOD)) % MOD
        
            if hay_hash == needle_hash:
                for j in range(n):
                    if haystack[i + j] != needle[j]:
                        break
                
                if j == n - 1:
                    return i
        
        return -1




