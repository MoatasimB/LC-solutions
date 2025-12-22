class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        

        n = len(nums)
        ans = 0
        for i in range(n - 2, -1, -1):
            nextNum = nums[i + 1]
            curr = nums[i]

            if nextNum >= curr:
                continue
            
            if curr % nextNum == 0:
                numElements = curr // nextNum
                ans += numElements - 1

                nums[i] = curr // numElements
            
            else:
                numElements = math.ceil(curr / nextNum)
                ans += numElements - 1
                nums[i] = curr // numElements
        
        return ans

