class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        ranges = []
        if nums[0] != lower:
            ranges.append([lower, nums[0] - 1])
        
        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                ranges.append([nums[i-1] + 1, nums[i] - 1])
            
        
        if nums[-1] != upper:
            ranges.append([nums[-1] + 1, upper])
        
        return ranges
