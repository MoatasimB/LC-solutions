class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def dfs(i, curr):
            print(curr)
            ans.append(curr[:])
            if i == len(nums):
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()
            # curr.append(nums[i])
            # dfs(i+1, curr)
            # curr.pop()

            # dfs(i+1, curr)
        
        dfs(0,[])
        return ans

