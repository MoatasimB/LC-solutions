class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        hashes = defaultdict(int)
        p = 31
        MOD = 10**9 + 7

        for word in words:
            n = len(word)
            preH = 0
            sufH = 0
            mult = 1
            for i in range(n):
                preChar = ord(word[i]) - ord('a') + 1
                sufChar = ord(word[n- i - 1]) - ord('a') + 1
                preH = (preH*p + preChar) % MOD
                sufH = (sufH + sufChar*mult) % MOD
                mult = (mult * p) % MOD

                if preH == sufH and preH in hashes:
                    ans+= hashes[preH]
                
            hashes[preH] += 1
        return ans

  