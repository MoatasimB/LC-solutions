class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        inDeg = defaultdict(int)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
            inDeg[x] += 1
            inDeg[y] += 1
        ans = []

        seen = set()

        def dfs(node):
            ans.append(node)

            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        for node in inDeg.keys():
            if inDeg[node] == 1 and node not in seen:
                seen.add(node)
                dfs(node)
        
        return ans