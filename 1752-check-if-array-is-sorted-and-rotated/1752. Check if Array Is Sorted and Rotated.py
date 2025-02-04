class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) <=1:
            return True
        switch = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                switch +=1
        
        if nums[-1] > nums[0]:
            switch +=1
        return switch == 1 or switch == 0
