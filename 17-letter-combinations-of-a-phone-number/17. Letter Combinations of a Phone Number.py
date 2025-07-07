class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mpp = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        if not digits:
            return []
        ans = []
        def dfs(i, curr):
            if i == len(digits):
                ans.append("".join(curr[:]))
                return
            
            for ch in mpp[digits[i]]:
                curr.append(ch)

                dfs(i+1, curr)

                curr.pop()
        dfs(0,[])
        return ans