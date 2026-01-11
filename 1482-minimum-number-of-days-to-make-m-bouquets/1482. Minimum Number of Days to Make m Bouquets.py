class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def check(day):
            count = 0
            curr = 0

            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    curr += 1
                    if curr == k:
                        count += 1
                        curr = 0
                else:
                    curr = 0
            
            return count >= m

        
        l = min(bloomDay)
        r = max(bloomDay)
        ans = r
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans