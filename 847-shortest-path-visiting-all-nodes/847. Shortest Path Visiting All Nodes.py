class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        ending = (1 << n) - 1
        q = deque()
        seen = set()
        for node in range(n):
            q.append((node, 1 << node, 0))
            seen.add((node, 1 << node))

        while q:
            node, mask, steps = q.popleft()

            if mask == ending:
                return steps

            for nei in graph[node]:
                if (nei, mask | (1 << nei)) not in seen:

                    q.append((nei,mask | (1 << nei), steps + 1))
                    seen.add((nei, mask | (1 << nei)))
        


        