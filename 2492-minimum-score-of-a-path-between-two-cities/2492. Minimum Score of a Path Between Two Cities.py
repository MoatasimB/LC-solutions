class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for x,y,dist in roads:
            graph[x].append([y, dist])
            graph[y].append([x, dist])

        # ans = float("inf")
        # seen = set()
        # path = set()
        # def dfs(node, pathWeight):
        #     if node == n:
        #         nonlocal ans
        #         ans = min(ans, pathWeight)
        #     seen.add(node)
        #     path.add(node)
        #     for nei, w in graph[node]:
        #         if nei in 
            


        
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
                


