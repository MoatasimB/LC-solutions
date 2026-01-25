class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        #curr node dist from X, Y, Z
        dists = [[] for _ in range(n)]

        
        def bfs(start):
            seen = set()
            q = deque()
            seen.add(start)
            q.append([start, 0])

            while q:
                node, dist = q.popleft()
                dists[node].append(dist)

                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append([nei, dist + 1])

        bfs(x)
        bfs(y)
        bfs(z)
        # print(dists)

        for arr in dists:
            arr.sort()

        # print(dists)
        ans = 0

        for a, b, c in dists:
            if a**2 + b **2 == c**2:
                ans += 1

        return ans

        