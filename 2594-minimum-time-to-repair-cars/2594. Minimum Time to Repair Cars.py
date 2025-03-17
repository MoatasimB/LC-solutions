class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        # time taken = rank * (carfinished)^2

        def check(mid):

            c = 0
            for rank in ranks:
                c += int(math.sqrt(mid // rank ))

            return c >= cars
        
        left = 0
        right = max(ranks) * (cars**2)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid -1
            else:
                left = mid + 1
            
        
        return left