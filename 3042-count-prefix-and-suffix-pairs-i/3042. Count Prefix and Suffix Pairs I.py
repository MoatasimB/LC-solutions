class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        p = 31
        MOD = 10**9 + 7
        hashes = defaultdict(int)
        ans = 0
        for word in words:
            n = len(word)
            preH = 0
            sufH = 0
            mult = 1
            for i in range(n):
                ch_pre = ord(word[i]) - ord('a') + 1
                ch_suf = ord(word[n-i-1]) - ord('a') + 1
                preH = (preH * p + ch_pre) % MOD
                sufH =(sufH + ch_suf * mult) % MOD
                mult = (mult * p) % MOD

                if preH == sufH and preH in hashes:
                    ans += hashes[preH]
                
            hashes[preH] += 1

        return ans