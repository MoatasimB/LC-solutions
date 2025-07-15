class Solution:
    def numTrees(self, n: int) -> int:
        

    #     return int((1 / (n + 1)) * math.comb(2*n, n))

    
        g = [0] * (n + 1)
        g[0] = 1
        g[1] = 1
        

      
        for i in range(2, n + 1):
            for j in range(1, i+1):
                left = j - 1
                right = i - j
                g[i] += g[left] * g[right]
        
        return g[n]
