class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        

        n = len(nums)

        
        ans = []
        if n == 0:
            return [[lower, upper]]

        if lower != nums[0]:
            missing = nums[0] - 1
            
            ans.append([lower, missing])
        

        for i in range(n - 1):
            curr = nums[i]
            nxt = nums[i + 1]
            if curr + 1 != nxt:
                missing = nxt - 1
                ans.append([curr + 1, missing])

        if upper != nums[-1]:
            ans.append([nums[-1] + 1, upper])
        
        return ans