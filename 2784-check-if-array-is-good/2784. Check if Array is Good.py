class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        n = len(nums)
        mpp = defaultdict(int)
        
        for i in range(n):
            mpp[nums[i]] += 1
            
        max_el = max(mpp.keys())
        for i in range(1, max_el):
            if i not in mpp or mpp[i] != 1:
                return False
        
        return mpp[max_el] == 2
