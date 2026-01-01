class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        ans = 0
        for i in range(len(strs[0])):
            prev = strs[0][i]
            for word in strs[1:]:
                if prev > word[i]:
                    ans += 1
                    break
                else:
                    prev = word[i]
        
        return ans
