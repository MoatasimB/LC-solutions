class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = float("inf")
        for i in range(len(strs) - 1):
            w1 = strs[i-1]
            w2 = strs[i]

            minLen = min(len(w1), len(w2))

            curr = 0
            for j in range(minLen):
                if w1[j] != w2[j]:
                    break
                curr += 1
            ans = min(ans, curr)
        
        return strs[0][:ans] if ans != float('inf') else ""

