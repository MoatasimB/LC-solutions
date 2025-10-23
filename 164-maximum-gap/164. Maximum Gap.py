class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        class Bucket:
            def __init__(self):
                self.used = False
                self.min = float("inf")
                self.max = float("-inf")
        
        if len(nums) < 2:
            return 0

        n = len(nums)
        maxi = max(nums)
        mini = min(nums)

        bucketSize = max(1,(maxi - mini) //( n - 1))
        bucketNums = (maxi - mini) // bucketSize + 1

        buckets = [Bucket() for _ in range(bucketNums)]

        for num in nums:
            idx = (num - mini) // bucketSize

            buckets[idx].used =True
            buckets[idx].min = min(num, buckets[idx].min)
            buckets[idx].max = max(num, buckets[idx].max)
        

        prev = mini
        maxGap = 0

        for bucket in buckets:
            if not bucket.used:
                continue
            
            maxGap = max(maxGap, bucket.min - prev)
            prev = bucket.max
        
        return maxGap
