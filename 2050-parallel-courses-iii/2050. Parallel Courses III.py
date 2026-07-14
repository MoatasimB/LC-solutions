class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        

        graph = defaultdict(list)
        indeg = [0] * n
        earliest = [0] * n
        for a, b in relations:
            graph[a - 1].append(b - 1)
            indeg[b - 1] += 1
        
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                earliest[i] = time[i]
                q.append([i, time[i]])
        
        ans = max(time)
        while q:
            node, curr = q.popleft()
            
            for nei in graph[node]:
                indeg[nei] -= 1
                earliest[nei] = max(earliest[nei], curr)
                if indeg[nei] == 0:
                    earliest[nei] += time[nei]
                    q.append([nei, earliest[nei]])

        return max(earliest)



        #     q_len = len(q)
        #     levelTime = 0
        #     neighbors = set()
        #     for _ in range(q_len):
        #         node, curr = q.popleft()
        #         levelTime = max(levelTime, curr)

        #         for nei in graph[node]:
        #             indeg[nei] -= 1
        #             neighbors.add(nei)
            
        #     for nei in neighbors:
        #         if indeg[nei] == 0:
        #             q.append([nei, levelTime + time[nei]])
        #             ans = max(ans, levelTime + time[nei])
        # return ans


        # #max time of my prereqs + my time = earliest time I can finish my course

        
