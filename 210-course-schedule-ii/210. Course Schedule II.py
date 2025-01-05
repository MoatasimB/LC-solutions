class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for second, first in prerequisites:
            indegree[second] +=1
            adj[first].append(second)
        
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()

            ans.append(node)
            
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ans if len(ans) == numCourses else []