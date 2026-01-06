class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        
        
        
        
        MOD = 10**9 + 7
        base = 29

        # 29^3(b) + 29^2(a) + 29^1(n) + 29^0(a)

        def check(length):
            max_power = 1
            for _ in range(length):
                max_power *= base % MOD
            curr = 0
            seen = {} #hsh : idx where seen
            for i in range(length):

                curr = (curr * base + (ord(s[i]) - ord("a") + 1)) % MOD
            
            seen[curr] = s[:length]
            l = 0
            for r in range(length, len(s)):
                curr = (curr * base + (ord(s[r]) - ord("a") + 1)) % MOD
                curr = (curr - ((max_power * (ord(s[l]) - ord("a") + 1)) % MOD)) % MOD
                l += 1
                if curr in seen and s[l:r + 1] == seen[curr]:
                    return [True, seen[curr]]
                
                seen[curr] = s[l:r + 1]
            
            return [False, ""]
        
        l = 1
        r = n - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2

            valid, word = check(mid)
            if valid:
                ans = word
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
        

