class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for x,y,dist in roads:
            graph[x].append([y, dist])
            graph[y].append([x, dist])
        ans = float("inf")
        seen = set()
        seen.add(1)
        def dfs(node):
            nonlocal ans
            for nei, w in graph[node]:
                ans = min(ans, w)
                if nei not in seen:
                    seen.add(node)
                    dfs(nei)
        dfs(1)
        return ans



        
        pathDists = [float("inf")] * (n + 1)
        minHeap = [[float("inf"), 1]] #pathdist, node

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if dist > pathDists[node]:
                continue
            
            for nei, w in graph[node]:
                newDist = min(w, dist)
                if newDist < pathDists[nei]:
                    pathDists[nei] = newDist
                    heapq.heappush(minHeap, [newDist, nei])
        
        return pathDists[n]
                


