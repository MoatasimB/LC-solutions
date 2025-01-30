class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for i in range(len(rooms)):
            for key in rooms[i]:
                adj[i].append(key)
        
        def dfs(node):
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        def bfs(node):
            q = deque()
            q.append(node)

            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
        
        seen = set()
        bfs(0)
        seen.add(0)

        return len(seen) == len(rooms)