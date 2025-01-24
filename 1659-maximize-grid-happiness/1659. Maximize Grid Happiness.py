class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        
        dp = {}
        scores = {
                    (0,1): 0,
                    (0, 2): 0,
                    (1, 2): -10,
                    (2,1): -10,
                    (2,2): 40,
                    (1,1): -60,
                            }

        def dfs(i, mem, intCount, extCount):

            if i == m*n or intCount + extCount == 0:
                return 0
            
            if (i,mem,intCount,extCount) in dp:
                return dp[(i,mem,intCount,extCount)]
            
            up = mem[0]
            left = mem[-1]
            
            ans = dfs(i+1, mem[1:] + tuple([0]), intCount, extCount)

            j = i % n

            if extCount:
                curr = 40+ scores[(up, 2)] + bool(j) * scores[(left, 2)]
                ans = max(ans, curr + dfs(i+1, mem[1:] + tuple([2]), intCount, extCount - 1))
            if intCount:
                curr = 120 + scores[(up, 1)] + bool(j) * scores[(left, 1)]
                ans = max(ans, curr + dfs(i+1, mem[1:] + tuple([1]), intCount - 1, extCount))
            
            dp[(i,mem,intCount,extCount)] = ans
            return ans

        mem = tuple([0 for _ in range(n)])
        return dfs(0, mem, introvertsCount, extrovertsCount)
