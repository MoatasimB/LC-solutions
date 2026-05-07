class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prev_max = []

        prev = (float("-inf"), -1)
        for i in range(n):
            if nums[i] > prev[0]:
                prev = (nums[i], i)
            prev_max.append(prev)
        ans = [0] * n
        def dfs(idx, rightMin, rightMax):
            p_max, pivot_idx = prev_max[idx]
            curr_max = rightMax if rightMin < p_max else p_max

            new_min = min(p_max, rightMin)

            for i in range(pivot_idx, idx + 1):
                new_min = min(new_min, nums[i])
                ans[i] = curr_max
            
            if pivot_idx == 0:
                return 
            
            dfs(pivot_idx - 1, new_min, curr_max)
        
        dfs(n - 1, float("inf"), 0)
        return ans

        
        #we have all the numbers from the left now

        #all small numbers have their value from the left
        #all that is left is to check if there is a number to the right smaller than current number but has a greater number than what we have saved
       