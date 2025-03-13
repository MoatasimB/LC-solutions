class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        l = 1
        r = sum(ribbons)

        if k > r:
            return 0
        
        def check(mid):
            count = 0

            for size in ribbons:
                count += (size // mid )
            
            return count >= k
        
        ans = float("-inf")
        while l <= r:
            mid = (l+r) // 2

            if check(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1

        return ans if ans!= float("-inf") else 0