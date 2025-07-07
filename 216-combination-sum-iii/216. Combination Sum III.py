class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = [1,2,3,4,5,6,7,8,9]
        
        # curr = [13]
        # start =2 
        # sum = 4
        
        def backtrack(curr, start, s):
            
            if len(curr) == k and s==n:
                ans.append(curr[:])
                return
                
            for j in range(start, len(digits)):
                if s + digits[j] <= n:
                    curr.append(digits[j])
                    backtrack(curr, j+1 ,s+digits[j])
                    curr.pop()
        
        
        ans = []
        backtrack([],0,0)

        return ans
        
            