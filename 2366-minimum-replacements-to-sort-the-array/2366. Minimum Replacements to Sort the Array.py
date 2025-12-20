class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        

        ans = 0
        n = len(nums)

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            
            if nums[i] % nums[i + 1] == 0:
                elements = nums[i] // nums[i + 1]

                ans += elements - 1
                nums[i] = nums[i] // elements
            else:
                elements = math.ceil(nums[i] / nums[i + 1])

                ans += elements - 1

                nums[i] = nums[i] // elements
        
        return ans
