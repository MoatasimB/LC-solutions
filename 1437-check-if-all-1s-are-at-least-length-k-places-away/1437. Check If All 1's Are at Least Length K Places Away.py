class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastOne = float("-inf")
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - lastOne - 1 < k:
                    return False
                lastOne = i
        
        return True
