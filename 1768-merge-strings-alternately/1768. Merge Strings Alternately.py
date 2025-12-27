class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = []

        i = 0
        j = 0

        n1 = len(word1)
        n2 = len(word2)

        while i < n1 or j < n2:
            
            if i < n1:
                ans.append(word1[i])
                i += 1
            if j < n2:
                ans.append(word2[j])
                j += 1
        
        return "".join(ans)