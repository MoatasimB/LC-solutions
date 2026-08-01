class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        memo = {}
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            score = float("-inf")
            curr = 0
            score = max(score, nums[i] - dfs(i + 1, j))
            score = max(score, nums[j] - dfs(i, j - 1))
            memo[(i, j)] = score
            return score
        
        n = len(nums)

        final = dfs(0, n - 1)
        return final >= 0
        