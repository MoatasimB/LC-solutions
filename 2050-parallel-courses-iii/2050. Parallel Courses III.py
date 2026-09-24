class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        
        if n == 1:
            return time[0]
        graph = defaultdict(list)
        indeg = [0] * (n + 1)
        timeForNode = defaultdict(int)
        for i in range(len(relations)):
            a, b = relations[i]
            graph[a].append(b)
            indeg[b] += 1
            timeForNode[b] = max(timeForNode[b], time[a - 1])

        q = deque()
        print(indeg)
        print(time)
        for i in range(1, n + 1):
            if indeg[i] == 0:
                q.append([i, 0]) #node, time to this node
        ans = 0
        
        while q:
            node, t = q.popleft()
            timeOfNode = time[node - 1]
            ans = max(ans, t +timeOfNode )
            for nei in graph[node]:
                #time to neighbor will be max of time to prevNode + timeOfNode
                indeg[nei] -= 1
                timeForNode[nei] = max(timeForNode[nei], t + timeOfNode)
                if indeg[nei] == 0:
                    q.append([nei, timeForNode[nei]])
        return ans
        # print(q)
        # while q:
        #     print("q", q)
        #     q_len = len(q)
        #     max_t = 0
        #     for _ in range(q_len):
        #         course = q.popleft()
        #         max_t = max(max_t, time[course - 1])
        #         print("course", course)
        #         for nei in graph[course]:
        #             indeg[nei] -= 1
        #             if indeg[nei] == 0:
        #                 q.append(nei)
            
        #     ans += max_t
        #     print(ans)
        
        # return ans if sum(indeg) == 0 else -1

