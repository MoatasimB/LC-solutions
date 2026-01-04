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
        
        memo = {}
        def dfs(string, i):
            if (string, i) in memo:
                return memo[(string, i)]
            if i == len(key):
                return 0
            
            ans = float("inf")
            ch = key[i]
            #go clockwise
            clockWiseCount, clockWiseString = clockWise(string, ch)
            ans = min(ans, clockWiseCount + dfs(clockWiseString, i + 1))
            


            #go anticlockwise
            antiClockWiseCount, antiClockWiseString = antiClockWise(string, ch)
            ans = min(ans, antiClockWiseCount + dfs(antiClockWiseString, i + 1))

            memo[(string, i)] = ans
            return ans

        return dfs(ring, 0)