class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def getSum(x: int) -> int:
            ans = 0
            while x:
                ans += (x % 10)
                x = x // 10
            
            return ans
        n = len(nums)
        for i in range(n):
            if i == getSum(nums[i]):
                return i
        
        return -1