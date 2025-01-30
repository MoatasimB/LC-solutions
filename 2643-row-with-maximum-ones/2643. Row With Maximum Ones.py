class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        ans = float('inf')
        currMax = float('-inf')
        for i in range(len(mat)):
            curr = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    curr +=1
            
            if curr > currMax:
                currMax = curr
                ans = i
        
        return [ans, currMax]
