class Solution:
    def countGoodNumbers(self, n: int) -> int:


        MOD = 10**9 +7

        def pow(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return pow(x*x % MOD, n // 2) % MOD
            else:
                return (x * pow((x*x) % MOD, n // 2)) % MOD
        
        if n % 2 == 0:
            evens = n // 2
            primes = n // 2
        else:
            evens = n //2 + 1
            primes = n//2 
        return (pow(5, evens) * pow(4, primes)) % MOD
        # 0 1 2 3
        # _ _ _ _ 
        # 4 4 5 4