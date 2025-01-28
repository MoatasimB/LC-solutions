class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def dfs(i, curr):
            print(curr)
            if i == len(nums):
                ans.append(curr[:])
                return 

            
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()

            
            while i+1 <len(nums) and nums[i] == nums[i+1]:
                i +=1
            
            dfs(i+1, curr)
        
        dfs(0,[])
        return ans