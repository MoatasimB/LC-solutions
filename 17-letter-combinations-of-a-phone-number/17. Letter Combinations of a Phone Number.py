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


        ans = []
        if not digits:
            return []
        def dfs(i, curr):

            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return
            
            for j in range(i, len(digits)):
                for d in mpp[digits[j]]:
                    curr.append(d)
                    dfs(j+1, curr)
                    curr.pop()
        

        dfs(0,[])
        return ans
