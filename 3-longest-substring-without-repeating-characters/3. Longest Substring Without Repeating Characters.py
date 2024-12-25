class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)

        l = 0
        ans = 0
        for r in range(len(s)):

            while s[r] in dic:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l+=1
            
            dic[s[r]] +=1
            ans = max(ans, r-l+1)
        return ans
