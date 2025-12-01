class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        def twoSum(curr, l):
            r = len(nums) - 1
            
            while l < r:
                
                if nums[l] + nums[r] + curr == 0:
                    ans.append([curr, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] + curr > 0:
                    r -= 1
                else:
                    l += 1

                
        
        i = 0
        
        while i < len(nums) - 1:
            
            
            if i < len(nums) - 1:
                twoSum(nums[i], i + 1)
            
            while i < len(nums) -1 and nums[i] == nums[i + 1]:
                i += 1
        
            i += 1
        
        return ans
    
    [0,0,0,0]
    
    