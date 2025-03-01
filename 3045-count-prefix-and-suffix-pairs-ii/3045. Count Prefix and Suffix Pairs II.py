class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        p = 31
        mod = 10**9 + 7
        hashes = defaultdict(int)

        ans = 0

        for word in words:
            n = len(word)
            preH = 0
            sufH = 0
            mult = 1

            for i in range(n):
                preC = ord(word[i]) - ord('a') + 1
                suffC = ord(word[n-i-1]) - ord('a') + 1
                preH = (preH*p + preC) % mod
                sufH = (sufH + suffC*mult) %mod
                mult = (mult * p) % mod
            
                if preH == sufH and preH in hashes:
                    ans += hashes[preH]
            
            hashes[preH] += 1
        
        return ans