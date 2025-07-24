class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append([v,w])

        signalTimeRec = {i + 1 : float("inf") for i in range(n)}
        pq = [[0, k]]

        while pq:
            time_rec, node = heapq.heappop(pq)

            if time_rec >= signalTimeRec[node]:
                continue
            
            signalTimeRec[node] = time_rec

            for nei, weight in graph[node]:
                heapq.heappush(pq, [time_rec + weight, nei])
        
        ans = float('-inf')
        for node, time_rec in signalTimeRec.items():
            ans = max(ans, time_rec)
        
        return ans if ans != float('inf') else -1


