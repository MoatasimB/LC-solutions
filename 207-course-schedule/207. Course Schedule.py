class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adj = defaultdict(list)

        for x, y in prerequisites:
            indeg[x] += 1
            adj[y].append(x)
        
        q = deque()
        
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()

            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return sum(indeg) == 0
