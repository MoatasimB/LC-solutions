class Solution:
    def numTrees(self, n: int) -> int:
        
        F = [0] * (n + 1)
        F[1] = 1
        F[0] = 1

        for i in range(2, n + 1):
            for j in range(1, i+1):
                F[i] += F[j - 1] * F[i - j]
        
        return F[n]


        
