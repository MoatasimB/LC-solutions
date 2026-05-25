class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = {i:[] for i in range(n)}

        def findNeighbors(idx, n):
            curr = arr[idx]

            start = idx
            for _ in range(d):
                start -= 1
                if start < 0:
                    break
                if arr[start] >= curr:
                    start += 1
                    break
                graph[idx].append(start)
            end = idx
            for _ in range(d):
                end += 1
                if end >= n:
                    break
                if arr[end] >= curr:
                    end -= 1
                    break
                graph[idx].append(end)
        
        for i in range(n):
            findNeighbors(i, n)

        memo = {}

        for key, lst in graph.items():
            if len(lst) == 0:
                memo[key] = 1
        print(graph)
        print(memo)
        def dfs(i):
            if i in memo:
                return memo[i]
            curr = float("-inf")
            for nei in graph[i]:
                # print(i, nei)
                curr = max(curr, 1 + dfs(nei))
            
            memo[i] = curr
            return memo[i]
        
        for i in range(n):
            if i not in memo:
                dfs(i)
        return max(memo.values())

            

