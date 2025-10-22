class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(x):
            
            curr = 0
            for n in nums:
                curr += math.ceil(n/x)
            
            return curr <= threshold
        
        left = 1
        right = max(nums)
        
        while left <= right:
            
            mid = (left + right) //2
            
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
            