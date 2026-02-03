class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        # [1,3,5,4,2,6]
        #  p 
        #    q

        for p in range(1, n):
            for q in range(p + 1, n - 1):

                valid = True
                for i in range(p + 1):
                    if i > 0 and nums[i - 1] >= nums[i]:
                        valid = False
                        break
                if valid:
                    for i in range(p, q):
                        if nums[i] <= nums[i + 1]:
                            valid = False
                            break
                if valid:
                    for i in range(q, n - 1):
                        if nums[i] >= nums[i + 1]:
                            valid = False
                            break
                if valid:
                    # print(p, q)
                    return True
        
        return False
