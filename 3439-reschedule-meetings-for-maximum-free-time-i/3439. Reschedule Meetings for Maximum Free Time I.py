class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        n = len(startTime)
        free = [0] * (n)

        free[0] = startTime[0]

        for i in range(1, n):
            free[i] = startTime[i] - endTime[i-1]
        
        free.append(eventTime - endTime[-1])

        ans = curr = sum(free[: k+ 1])

        for i in range(k+1, n+1):
            curr += free[i] - free[i-k-1]
            ans = max(ans, curr)
        return ans