class Solution:
    def numOfWays(self, n: int) -> int:
        
        MOD = 10**9 + 7

        memo = {}
        def dfs(i, p1, p2, p3):
            if (i, p1, p2, p3) in memo:
                return memo[(i, p1, p2, p3)]
            if i == n:
                return 1
            
            total = 0
            for c1 in range(3):
                if c1 == p1:
                    continue

                for c2 in range(3):
                    if c2 == c1 or c2 == p2:
                        continue

                    for c3 in range(3):
                        if c3 == c2 or c3 == p3:
                            continue

                        total += dfs(i + 1, c1, c2, c3)

            memo[(i, p1, p2, p3)] = total % MOD
            return total % MOD
        
        return dfs(0, -1, -1, -1)
                


