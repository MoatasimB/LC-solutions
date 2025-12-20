class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #[.   x  n, n - 1, n - 2, n - 3]
        def swap(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = 0
        j = len(nums) - 2

        while j >= 0:
            nextNum = nums[j + 1]
            currNum = nums[j]

            if nextNum <= currNum:
                j -= 1
                continue
            else:
                #currNum is smaller
                #find the first num from the end that is greater than it
                x = len(nums) - 1

                while x >= 0 and nums[x] <= currNum:
                    x -= 1
                
                nums[x], nums[j] = nums[j], nums[x]
                swap(j + 1, len(nums) - 1)
                return
        
        i = 0
        j = len(nums) - 1

        swap(i, j)
        

  