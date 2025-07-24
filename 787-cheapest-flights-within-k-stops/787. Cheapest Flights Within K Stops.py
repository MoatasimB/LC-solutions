class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for s, d, c in flights:
            graph[s].append([d,c])

        seen = {i:float("inf") for i in range(n)} #node : cost
        q = deque()
        q.append([src,0]) #node, cost
        
        for _ in range(k + 2):
            len_q = len(q)
            for _ in range(len_q):
                node, cost = q.popleft()
                if cost >= seen[node]:
                    continue
                seen[node] = cost

                for nei, c in graph[node]:
                    q.append((nei, cost + c))
        
        return seen[dst] if seen[dst] != float('inf') else -1
            



        # stops_taken = {i:[0,float('inf')] for i in range(n) } #node : [stops, cost]

        # q = deque()

        # q.append([src,0,0]) #node, stops, cost

        # while q:
        #     node, stops, cost = q.popleft()

        #     if stops_taken[node][0] > k or stops_taken[node][1] < cost:
        #         continue
            
        #     stops_taken[node][0] = stops
        #     stops_taken[node][1] = cost


        #     for nei, c in graph[node]:
        #         q.append([nei, stops + 1, cost + c])
        


        # return stops_taken[dst][1] if stops_taken[dst][1] != float('inf') else -1

        