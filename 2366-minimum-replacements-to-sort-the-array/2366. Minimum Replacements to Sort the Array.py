class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        for i in range(n - 2, -1, -1):
            curr = nums[i]
            nextN = nums[i + 1]

            if curr > nextN:
                numElements = curr // nextN if (curr % nextN) == 0 else math.ceil(curr / nextN)
                
                nums[i] = curr // numElements
                ans += numElements - 1
        
        return ans