class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        par = ["(", ")"]
        

        
        def backtrack(curr, right, left):
            
            if len(curr) == n*2:
                ans.append("".join(curr[:]))
                return
            
            for p in par:
                if p == ")" and right >= left:
                    continue
                if p == "(" and left >= n:
                    continue
                curr.append(p)
                if p == "(":
                    left += 1
                else:
                    right +=1
                backtrack(curr, right, left)
                x = curr.pop()
                if x == "(":
                    left -= 1
                else:
                    right -=1
 
        
        ans = []
        backtrack([],0,0)
        return ans
        
        
        
        
        