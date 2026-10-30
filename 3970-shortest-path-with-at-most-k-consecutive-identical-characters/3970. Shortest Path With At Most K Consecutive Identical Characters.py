class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append([v, w])
        
        
        
        dists = [[float("inf")] * (k + 1) for _ in range(n)]
        dists[0][1] = 0
        minHeap = [[0, 0, 1]] #edge weight, node, length of consec
        
        while minHeap:
            curr, node, len_so_far = heapq.heappop(minHeap)
            if curr > dists[node][len_so_far]:
                continue
            
            for nei, w in graph[node]:
                nei_letter = labels[nei]
                if nei_letter == labels[node]:
                    new_len_so_far = len_so_far +  1
                else:
                    new_len_so_far = 1

                if new_len_so_far <= k and w + curr < dists[nei][new_len_so_far]:
                    dists[nei][new_len_so_far] = w + curr
                    heapq.heappush(minHeap, [w + curr, nei, new_len_so_far])
        ans = min(dists[n - 1])
        return ans if ans != float("inf") else -1
