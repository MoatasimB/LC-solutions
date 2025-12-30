class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        def dfs(i, curr):
            if i == len(s):
                ans.append(" ".join(curr[:]))
                return
            

            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word in wordDict:
                    curr.append(word)
                    dfs(j + 1, curr)
                    curr.pop()
        

        dfs(0, [])
        return ans
            