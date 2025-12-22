class Solution:
    def romanToInt(self, s: str) -> int:
        
        mpp = {
            "I":1,
            "V":5,
            "X":10,
            "L"  :50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        ans = 0

        for i in range(len(s)):
            if i + 1 < len(s) and mpp[s[i + 1]] > mpp[s[i]]:
                ans -= mpp[s[i]]
            else:
                ans += mpp[s[i]]
        
        return ans