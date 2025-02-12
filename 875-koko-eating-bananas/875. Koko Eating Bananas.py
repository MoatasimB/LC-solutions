class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(mid):

            count = 0

            for i in range(len(piles)):
                count += math.ceil(piles[i] / mid)

            return count <= h
        
        piles.sort()

        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = (r + l ) // 2

            if check(mid):
                r = mid - 1
                ans = min(mid, ans)
            else:
                l = mid + 1
        

        return ans
            