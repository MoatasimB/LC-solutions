class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        adj = defaultdict(list)
        deg = [0] * n
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            deg[x] += 1
            deg[y] += 1


        q = deque()

        for node, nei in adj.items():
            if len(nei) == 1:
                q.append(node)
        leaves = len(q)

        while n > 2:
            q_len = len(q)
            n -= len(q)
            for _ in range(q_len):
                node = q.popleft()
                for nei in adj[node]:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        q.append(nei)
            
        if n == 2:
            return [q[0], q[1]]
        if n == 1:
            return [q[0]]
            
            

