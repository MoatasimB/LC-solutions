class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        def get_components(node):
            q = deque()
            seen = set()
            q.append(node)

            seen.add(node)
            ans = 0
            while q:
                n = q.popleft()

                for nei in adj[n]:
                    if nei not in seen:
                        seen.add(nei)
                        visited.add(nei)
                        q.append(nei)
            
            return seen



        def bfs(start):
            q = deque()
            seen = {}
            q.append((start, 1))

            seen[start] = 1
            ans = 0
            while q:
                node, group = q.popleft()
                ans = max(ans, group)

                for nei in adj[node]:
                    if nei in seen:
                        if (seen[nei] == group):
                            return -1
                        continue
                    seen[nei] = group + 1
                    q.append((nei, group + 1))
            
            return ans

        final = 0
        visited = set()
        for node in range(1, n+1):
            ans = -1
            if node in visited:
                continue
            visited.add(node)
            components = get_components(node)
            print(components)
            for n in components:
                x = bfs(n)
                if x == -1:
                    return -1
                ans = max(ans, x)
            final += ans
        return final


