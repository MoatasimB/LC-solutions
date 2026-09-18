class Solution:
    def minBuildTime(self, blocks: list[int], split: int) -> int:
        
        n = len(blocks)
        blocks.sort(reverse=True)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]
        
        def dfs(i, w):
            if memo[i][w] != -1:
                return memo[i][w]
            if i == n:
                return 0
            if w == 0:
                return float("inf")
            if w >= n - i:
                return blocks[i]
            #we can split
            do_split = split + dfs(i, min(2 * w, n))
            #we can decide that this worker handles this block
            handle = max(blocks[i], dfs(i + 1, w - 1))
            memo[i][w] = min(do_split, handle)
            return min(do_split, handle)
        
        return dfs(0, 1)
