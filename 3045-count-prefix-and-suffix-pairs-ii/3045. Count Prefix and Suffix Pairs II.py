class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt=0
        hashes=defaultdict(int)
        base=31
        MOD=int(1e9+7)
        for word in words:
            n=len(word)
            phash,shash=0,0 # prefix hash, suffix hash
            multiplier=1
            for i in range(n):
                pchar=ord(word[i])-ord('a')+1 # prefix char
                schar=ord(word[n-1-i])-ord('a')+1 # suffix char
                phash=(phash*base+pchar)%MOD
                shash=(shash+schar*multiplier)%MOD
                multiplier=(multiplier*base)%MOD
                if phash==shash and phash in hashes:cnt+=hashes[phash]
            hashes[phash]+=1
            # print(cnt,hashes)
        return cnt
        
        ans = 0
        hashes = defaultdict(int)
        p = 31
        MOD = 10**7

        for word in words:
            n = len(word)
            preH = 0
            sufH = 0
            mult = 1
            for i in range(n):
                preChar = (ord(word[i]) - ord('a')) + 1
                sufChar = (ord(word[n-i - 1]) - ord('a')) + 1
                preH = (preH*p + preChar) % MOD
                sufH = (sufH + sufChar*mult) % MOD
                mult = (mult * p) % MOD

                if preH == sufH and preH in hashes:
                    ans+= hashes[preH]
                
            hashes[preH] += 1
        return ans

  