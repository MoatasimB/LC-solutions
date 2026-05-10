class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        

        # {
        #     0:[1,4,5]
        #     1:[3, 4, 5]
        #     2:[3]
        #     3:[5]
        #     4:[5]
        #     5:
          
        # }
        n = len(nums)
        #        2
        #          \
        # 0 -> 1 -> 3 -> 5
        #   \. |.    /
        #       4
            
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= target:
                    graph[i].append(j)
        
        final = -1
        stepsToReach = {i:float("-inf") for i in range(n)}
        
        def dfs(node, steps):
            if node == n - 1:
                nonlocal final
                final = max(final, steps)
                return
            if stepsToReach[node] > steps:
                return
            for nei in graph[node]:
                if stepsToReach[nei] < steps + 1:
                    stepsToReach[nei] = steps + 1
                    dfs(nei, steps + 1)
        
        dfs(0, 0)
        return final


        seen = set()
        q = deque()
        q.append([0, 0])

        final = -1
        while q:
            idx, step = q.popleft()

            if idx == n - 1:
                final = max(final, step)

            for nei in graph[idx]:
                    q.append([nei, step + 1])
        
        return final
