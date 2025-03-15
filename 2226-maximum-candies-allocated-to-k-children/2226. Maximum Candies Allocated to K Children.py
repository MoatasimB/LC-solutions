class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):
            count = 0
            for c in candies:
                count += c // mid
            
            return count >= k
        
        l = 1
        r = sum(candies)
        ans = float("-inf")
        while l <= r:
            mid = (l+r) // 2

            if check(mid):
                l = mid + 1
                ans = max(ans, mid)
            else:
                r = mid - 1
        
        return ans if ans != float("-inf") else 0