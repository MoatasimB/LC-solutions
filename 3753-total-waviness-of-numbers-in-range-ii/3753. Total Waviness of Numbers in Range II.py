class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(num):
            if num < 100:
                return 0
            
            str_num = str(num)
            n = len(str_num)
            memo = {}
            def dfs(pos, prev, curr, isLimit, isLeading):
                if pos == n:
                    return 1, 0
                if (pos, prev, curr, isLimit, isLeading) in memo:
                    return memo[(pos, prev, curr, isLimit, isLeading)]
                count = 0
                waviness = 0
                up = int(str_num[pos]) if isLimit else 9

                for d in range(up + 1):
                    newLeading = isLeading and (d == 0)
                    newPrev = curr
                    newCurr = -1 if newLeading else d
                    subCnt, subSum = dfs(pos + 1, newPrev, newCurr, isLimit and (d == up), newLeading)

                    if not newLeading and prev >= 0 and curr >= 0:
                        if (prev < curr and curr > d) or (prev > curr and curr < d):
                            waviness += subCnt

                    count += subCnt
                    waviness += subSum
                    memo[(pos, prev, curr, isLimit, isLeading)] = (count, waviness)
                return count, waviness
            
            return dfs(0, -1, -1, True, True)[1]
        
        return solve(num2) - solve(num1 - 1)
