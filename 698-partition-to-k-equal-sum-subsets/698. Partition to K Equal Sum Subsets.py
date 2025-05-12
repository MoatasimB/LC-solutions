class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False
        
        goal = total // k
        nums.sort(reverse = True)
        taken = ['0'] * len(nums)
        memo = {}
        def dfs(i, subsets, curr_sum):
            taken_memo = "".join(taken)
            if taken_memo in memo:
                return memo[taken_memo]
            if subsets == k - 1:
                return True
            if curr_sum > goal:
                return False
            if curr_sum == goal:
                memo[taken_memo] = dfs(0,subsets + 1, 0)
                return memo[taken_memo]

            for j in range(i, len(nums)):
                if taken[j] == '0':
                    taken[j] = '1'
                    if dfs(j + 1, subsets, curr_sum + nums[j]):
                        memo[taken_memo] = True
                        return memo[taken_memo]
                    taken[j] ='0'
            memo[taken_memo] = False
            return memo[taken_memo]        
        return dfs(0,0,0)

