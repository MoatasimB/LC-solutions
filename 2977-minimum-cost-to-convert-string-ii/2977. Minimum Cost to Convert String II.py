class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        _id = 0
        mpp = defaultdict(int)
        lengths = set()

        for i in range(len(original)):
            s1 = original[i]
            s2 = changed[i]
            mpp[s1] = _id
            _id += 1
            mpp[s2] = _id
            _id += 1
            lengths.add(len(s1))
        lengths = sorted(lengths)
        minCosts = [[float("inf")] * _id for _ in range(_id)]
        for i in range(len(original)):
            u = mpp[original[i]]
            v = mpp[changed[i]]
            minCosts[u][v] = min(minCosts[u][v], cost[i])
 
        for k in range(_id):
            for i in range(_id):
                if minCosts[i][k] < float("inf"):
                    for j in range(_id):
                        if minCosts[k][j] < float("inf"):
                            minCosts[i][j] = min(minCosts[i][j], minCosts[i][k] + minCosts[k][j])
        n = len(source)
        dp = [float("inf")] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            
            for l in lengths:
                end = i + l
                if end > n:
                    break
                s1 = source[i : end]
                s2 = target[i : end]
            # for j in range(i, n):
            #     s1 = source[i:j + 1]
            #     s2 = target[i:j + 1]
                if s1 in mpp and s2 in mpp:
                    c = minCosts[mpp[s1]][mpp[s2]]
                   
                    dp[i] = min(dp[i], c + dp[end])
        return dp[0] if dp[0] != float("inf") else -1

        # memo = {}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i == len(source):
        #         return 0
        #     total = float("inf")
        #     if source[i] == target[i]:
        #         total = dfs(i + 1)
        #     for j in range(i, len(source)):
        #         u = source[i:j + 1]
        #         v = target[i:j + 1]
        #         if u in mpp and v in mpp:
        #             c = minCosts[mpp[u]][mpp[v]]
        #             if c == float("inf"):
        #                 continue
        #             else:
        #                 total = min(total, c + dfs(j + 1))
        #     memo[i] = total
        #     return total
        
        # final = dfs(0)
        # return final if final != float("inf") else -1