class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dictionary = set(dictionary)
        memo = {}
        def dfs(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            if i == len(s):
                return curr
            

            ans = len(s)
            for j in range(i, len(s)):
                if s[i: j + 1] in dictionary:
                    ans = min(ans, dfs(j + 1, curr))
                ans = min(ans, dfs(j+1, curr + j - i +1 ))
            memo[(i, curr)] = ans
            return ans
        
        return dfs(0, 0)
