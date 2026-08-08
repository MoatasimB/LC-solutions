class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        for a, b in invocations:
            graph[a].append(b)
        
        seen = set()
        seen.add(k)
        def dfs(node):

            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        dfs(k)

        for a, b in invocations:
            if a not in seen and b in seen:
                return [i for i in range(n)]

        
        
        return [node for node in range(n) if node not in seen]