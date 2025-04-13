class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}

        
        for i in range(len(nums)):

            if target - nums[i] in mpp:
                return [i, mpp[target-nums[i]]]
            else:
                mpp[nums[i]] = i
