class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        ans = 0

        for num in nums:
            r = num % 3
            if r != 0:
                ans += 1
        
        return ans
            