class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        mpp = Counter(nums)
        n = len(nums)
        if k == len(nums):
            return max(nums)
        if k == 1:
            ans = float('-inf')
            for num, cnt in mpp.items():
                if cnt == 1:
                    ans = max(ans, num)
            return ans if ans != float('-inf') else -1
        
        if mpp[nums[0]] == 1 and mpp[nums[n - 1]] == 1:
            return max(nums[0], nums[n - 1])
        
        if mpp[nums[0]] == 1:
            return nums[0]
        
        elif mpp[nums[n - 1]] == 1:
            return nums[n-1]
        
        return -1

