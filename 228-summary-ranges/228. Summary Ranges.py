class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = nums[0]
        ans = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                continue
            if start != nums[i-1]:
                ans.append(f"{start}->{nums[i-1]}")
            else:
                ans.append(f"{nums[i-1]}")

            start = nums[i]
            print(start)
    
        if start != nums[-1]:
            ans.append(f"{start}->{nums[-1]}")
        else:
            ans.append(f"{nums[-1]}")
        
        return ans
