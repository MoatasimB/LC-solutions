class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if digits =="":
            return []
        def backtrack(curr,i):
            
            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return
            
            letters = dic[digits[i]]
            # for n in range(i,len(digits)):
            for l in letters:
                curr.append(l)
                backtrack(curr, i+1)
                curr.pop()
        ans = []
        backtrack([],0)
        # print(ans)
        return(ans)
