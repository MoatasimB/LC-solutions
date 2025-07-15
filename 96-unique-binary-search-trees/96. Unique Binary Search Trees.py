class Solution:
    def numTrees(self, n: int) -> int:
        

        return int((1 / ((2*n )+ 1)) * math.comb(2*n + 1, n))

        # count = 0
        # for i in range(n):
        #     left = i
        #     right = n - i - 1

        #     count += left * right
        
        # memo = {}
        # def dfs(n):

        #     if n == 1:
        #         return 1
            
        #     left = 