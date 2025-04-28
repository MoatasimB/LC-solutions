class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        i = 0
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        ans = 0
        beg = 0
        while i < len(nums) and beg < len(nums):
            if counts[nums[i]] > 1:
                for j in range(beg, min(beg+3, len(nums))):
                    counts[nums[j]] -= 1
                beg += 3
                ans += 1
                # i += 3
            else:
                i += 1
        return ans
            

