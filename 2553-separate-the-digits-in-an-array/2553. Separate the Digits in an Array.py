class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        digits = [[] for _ in range(n)]


        def make(d, idx):

            while d:
                digit = d % 10
                d = d // 10
                digits[idx].append(digit)
        

        for i in range(len(nums)):
            make(nums[i], i)
        

        ans = []

        for i in range(len(digits)):
            for j in range(len(digits[i]) - 1, -1, -1):
                ans.append(digits[i][j])
        
        return ans
