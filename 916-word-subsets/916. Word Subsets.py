class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for ch in word:
                ans[ord(ch) - ord('a')] +=1
            
            return ans

        bmax = [0] * 26
        for b in words2:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for word in words1:
            flag = True
            for i, c in enumerate(count(word)):
                if c < bmax[i]:
                    flag = False
                    break
            
            if flag:
                ans.append(word)
        
        return ans

                