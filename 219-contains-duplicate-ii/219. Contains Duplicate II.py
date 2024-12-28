class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        mpp = {}

        for i in range(len(nums)):
            if nums[i] in mpp:
                if abs(i - mpp[nums[i]]) <=k:
                    return True
            
            mpp[nums[i]] = i
        
        return False
