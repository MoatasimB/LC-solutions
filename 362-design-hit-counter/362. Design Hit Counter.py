class HitCounter:

    def __init__(self):
        self.nums = []
        

    def hit(self, timestamp: int) -> None:
        self.nums.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        start = max(0, timestamp - 300) + 1
        end = timestamp
        print(timestamp, start, end, self.nums)
        #smallet timestamp idx greater than start
        #largest timestamp idx less than end
        if not self.nums or self.nums[-1] < start:
            return 0
        l = 0
        r = len(self.nums) - 1
        firstIdx = r
        while l <= r:
            mid = (l + r) // 2

            if self.nums[mid] >= start:
                firstIdx = mid
                r = mid - 1
            else:
                l = mid + 1
        

        l = 0
        r = len(self.nums) - 1
        lastIdx = 0
        while l <= r:
            mid = (l + r) // 2

            if self.nums[mid] <= end:
                lastIdx = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return lastIdx - firstIdx + 1

        # start = 1
        # end = 301
        # [1 2 3 300]

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
 
#   304
# 5 - 304
#  [2 3 4]