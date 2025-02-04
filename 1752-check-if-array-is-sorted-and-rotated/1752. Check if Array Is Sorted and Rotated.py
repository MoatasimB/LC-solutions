class Solution:
    def check(self, nums: List[int]) -> bool:
        
        switch = 0
        curr = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                curr = i
                break
        print(curr)
        if curr == 0:
            return True

        while curr < len(nums) - 1:
            if nums[curr] > nums[0]:
                return False
            if not nums[curr] <=  nums[curr+1] :
                return False   
            curr +=1
        if nums[-1] > nums[0]:
            return False
        return True
