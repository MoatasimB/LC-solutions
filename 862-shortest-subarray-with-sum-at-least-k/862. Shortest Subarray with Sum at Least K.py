class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        prefix_sums = [0, nums[0]]

        for i in range(1, n):
            prefix_sums.append(prefix_sums[-1] + nums[i])
        
        indices = deque()
        ans = float('inf')

        for i in range(n + 1):

            while indices and prefix_sums[i] - prefix_sums[indices[0]] >= k:
                ans = min(ans, i - indices.popleft())
            

            while indices and prefix_sums[i] <= prefix_sums[indices[-1]]:
                indices.pop()
        
            indices.append(i)
        
        return -1 if ans == float('inf') else ans