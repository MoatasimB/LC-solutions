class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def dfs(i,curr):

            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                dfs(i, curr)
                curr.pop()
        
        dfs(0,[])
        return ans