class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        arr = [False] + [False] + [True] * (n-2)

        for i in range(2, int(sqrt(n)) + 1):

            if arr[i]:

                for multiple in range(i*i, n, i):
                    arr[multiple] = False
        return sum(arr)