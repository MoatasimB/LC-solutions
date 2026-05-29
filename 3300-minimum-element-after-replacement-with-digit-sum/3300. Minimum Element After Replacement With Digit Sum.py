class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        def getSum(num):
            ans = 0

            while num:
                ans += num % 10
                num  = num // 10
            return ans
        
        return min([getSum(x) for x in nums])