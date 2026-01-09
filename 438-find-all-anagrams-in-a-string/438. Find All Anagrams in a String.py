class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        mpp = defaultdict(int)
        for ch in p:
            mpp[ch] += 1
        
        need = len(mpp)
        ans = []
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in mpp:
                mpp[ch] -= 1
                if mpp[ch] == 0:
                    need -= 1
            
            if r >= len(p):
                ch = s[l]
                if ch in mpp:
                    mpp[ch] += 1
                    if mpp[ch] - 1 == 0:
                        need += 1
                l += 1
            if need == 0:
                ans.append(l)
        
        return ans
