class Solution:
    def firstUniqChar(self, s: str) -> int:
        mpp = {}
        for i in range(len(s)):
            if s[i] in mpp:
                mpp[s[i]] = False
            else:
                mpp[s[i]] = True

        
        for i in range(len(s)):
            if mpp[s[i]]:
                return i
        
        return -1