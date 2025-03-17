class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def check(mid):
            count = 0
            for r in ranks:
                x = int(math.sqrt(mid / r))
                # print(x, mid, r)
                count += x
            
            return count >= cars

        
        l = 1
        r = max(ranks) * (cars**2)
        ans = float('inf')
        while l <= r:
            mid = (l+r) // 2

            if check(mid):
                ans = min(mid,ans)
                r = mid - 1
            else:
                l = mid + 1
        
        return ans if ans else -1