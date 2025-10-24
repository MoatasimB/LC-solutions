class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        ending = (1 << n) - 1
        q = deque()
        seen = set()
        for node in range(n):
            q.append((node, 1 << node))
            seen.add((node, 1 << node))

        steps = 0
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node, mask = q.popleft()

                if mask == ending:
                    return steps

                for nei in graph[node]:
                    if (nei, mask | (1 << nei)) not in seen:
    
                        q.append((nei,mask | (1 << nei)))
                        seen.add((nei, mask | (1 << nei)))
            steps += 1
        


        