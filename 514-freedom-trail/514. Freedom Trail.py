class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        def clockWise(string, ch):
            q = deque([letter for letter in string])
            count = 0
            while q[0] != ch:
                count += 1
                q.appendleft(q.pop())
            
            return [count + 1, "".join(q)]
        
        def antiClockWise(string, ch):
            q = deque([letter for letter in string])
            count = 0
            while q[0] != ch:
                count += 1
                q.append(q.popleft())
            
            return [count + 1, "".join(q)]
        def countDistance(curr, next):
            dist = abs(curr - next)
            oppositeDist = len(ring) - dist
            return min(dist, oppositeDist) + 1
        memo = {}
        def dfs(string_idx, i):
            if (string_idx, i) in memo:
                return memo[(string_idx, i)]
            if i == len(key):
                return 0
            
            ans = float("inf")
            ch = key[i]

            for idx in range(len(ring)):
                if ring[idx] == ch:
                    ans = min(ans, countDistance(string_idx, idx) + dfs(idx, i + 1))
            


            # #go clockwise
            # clockWiseCount, clockWiseString = clockWise(string, ch)
            # ans = min(ans, clockWiseCount + dfs(clockWiseString, i + 1))
            


            # #go anticlockwise
            # antiClockWiseCount, antiClockWiseString = antiClockWise(string, ch)
            # ans = min(ans, antiClockWiseCount + dfs(antiClockWiseString, i + 1))

            memo[(string_idx, i)] = ans
            return ans

        return dfs(0, 0)