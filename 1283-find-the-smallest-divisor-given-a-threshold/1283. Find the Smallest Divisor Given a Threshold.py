class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check(mid):
            count = 0
            for num in nums:
                count += math.ceil(num/mid)
            return count <= threshold

        l = 1
        r = max(nums)
        ans = -1
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        
        return ans
