class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = nums[:]
        for num in nums:
            ans.append(num)
        
        return ans
