class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        

        #  6 4 7 3 2

        #  6 7 4 3 2
        #  6 7 2 3 4

    
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1

        if i == 0:
            l = 0
            r = n - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return 
        
        #i is the position of the place we need to replace
        j = n - 1
        i -= 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        

        #num to replace is at j

        nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        k = n - 1
        j = i + 1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1
        
        return

