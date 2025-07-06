class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def dfs(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()
        
        dfs([])
        return ans
