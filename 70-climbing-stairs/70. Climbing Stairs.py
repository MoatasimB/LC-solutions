class Solution:
    def climbStairs(self, n: int) -> int:
        
        twoBack = 1
        oneBack = 1

        curr = 0
        for i in range(2, n + 1):
            curr = oneBack + twoBack

            twoBack = oneBack
            oneBack = curr
            
        return oneBack