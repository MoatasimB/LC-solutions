class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        ans = []
        n = len(word)
        def dfs(i, curr, count):
            if i == n:
                if count > 0:
                    curr.append(str(count))

                ans.append("".join(curr[:]))
                if count > 0:
                    curr.pop()
                return
            
            dfs(i + 1, curr, count + 1)

            if count > 0:
                curr.append(str(count))
            curr.append(word[i])
            dfs(i + 1, curr, 0)
            curr.pop()
            if count > 0:
                curr.pop()
        dfs(0, [], 0)
        return ans