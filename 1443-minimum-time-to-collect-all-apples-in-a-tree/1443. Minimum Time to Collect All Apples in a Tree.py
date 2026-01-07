class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        def dfs(node, parent):
            nonlocal ans

            contains = hasApple[node]
            for child in graph[node]:
                if child == parent:
                    continue
                if dfs(child, node):
                    contains = True
                    ans += 2
            return contains
        dfs(0, -1)
        return ans

        