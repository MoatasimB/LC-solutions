class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        if n == 1: return (1<<k)-1
            
        for zeros in range(52):
            if (choices := comb(k+zeros-1,zeros)) >= n: return (1<<(k+zeros-1)) + self.nthSmallest(n,k-1)
            n -= choices