class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(mid):

            d = 0
            curr = 0
            for i in range(len(weights)):
                if weights[i] + curr > mid:
                    d +=1
                    curr = weights[i]
                    continue
                curr += weights[i]
            
            return d + 1 <= days
        
        l = max(weights)
        r = sum(weights)
        ans = float('inf')
        while l<=r:
            mid = (l+r) // 2
            if check(mid):
                ans = min(mid, ans)
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
