class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        def tSum(left, right, num):
            while left < right:
                if num + nums[left] + nums[right] > 0:
                    right -= 1
                elif num + nums[left] + nums[right] < 0:
                    left +=1
                else:
                    ans.append([num, nums[left], nums[right]])
                    right -=1
                    left +=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1


        while i < n:
            curr = nums[i]
            if curr > 0:
                break
            i+=1
            tSum(i, n-1, curr)
            while i < len(nums) - 1 and nums[i] == nums[i-1]:
                i+=1
        
        return ans


        
 