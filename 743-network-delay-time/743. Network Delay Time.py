class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append([v, w])

        pq = [[0,k]] #time, node
        seen = set()
        ans = float('-inf')
        while pq:

            time, node = heapq.heappop(pq)
            if node in seen:
                continue
            
            ans = max(ans, time)
            seen.add(node)

            for nei, v in graph[node]:
                heapq.heappush(pq, [time + v, nei])
        

        return ans if len(seen) == n else -1



        
        