class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        incomingEdges = defaultdict(list)

        for u, v, w in edges:
            graph[u].append([v, w])
            incomingEdges[v].append([u, 2*w])
        


        dists = [float("inf")] * n
        dists[0] = 0
        minHeap = [[0, 0]] #cost, node

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if dists[node] < cost:
                continue
            if node == n - 1:
                return cost
            
            for nei, c in graph[node]:
                if cost + c < dists[nei]:
                    dists[nei] = cost + c
                    heapq.heappush(minHeap, [cost + c, nei])
            
            for nei, c in incomingEdges[node]:
                if cost + c < dists[nei]:
                    dists[nei] = cost + c
                    heapq.heappush(minHeap, [cost + c, nei])


            
        
        return -1