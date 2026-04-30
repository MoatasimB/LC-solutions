class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i : [] for i in range(n)}
    
        for a, b in edges:
            graph[a].append(b)

        if (destination not in graph) or (source not in graph) or (len(graph[destination]) != 0):
            return False
        
        seen = set()
        path_seen = set()
        def dfs(node):
            # print(node)
            if len(graph[node]) == 0 and node != destination:
                return False
            if len(graph[node]) == 0 and node == destination:
                return True
            if node in seen:
                return True
            path_seen.add(node)
            seen.add(node)
            for nei in graph[node]:
                if nei not in path_seen:
                    if not dfs(nei):
                        return False
                elif nei in path_seen:
                    return False
                
            path_seen.remove(node)
            return True
        
        return dfs(source)
