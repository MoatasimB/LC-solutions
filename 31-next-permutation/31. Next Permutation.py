class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # go from back to front till numbers are not increasing
        # first number that is not increasing we want to switch
        #find the smallest number to the right that is greater than our number
        # reverse second half

        if len(nums) == 1:
            return

        i = len(nums) - 2
        while i > 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        
        if i == 0 and nums[0] == max(nums):
            nums.reverse()
            return
        
        smallestR = float('inf')
        j = len(nums) - 1
        idxSwitch = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                if nums[j] < smallestR:
                    smallestR = nums[j]
                    idxSwitch = j
            j -= 1
        
        nums[i], nums[idxSwitch] = nums[idxSwitch], nums[i]

        k = i + 1
        m = len(nums) - 1

        while k <= m:
            nums[k], nums[m] = nums[m], nums[k]
            k += 1
            m -= 1



        
        # 1 2 3 4

        # 1 2 4 3    

        # 1 3 2 4

        # 1 3 4 2

        # 1 4 2 3

        # 1 4 3 2

        # 2 1 3 4

        # 2 1 4 3

        # 2 

