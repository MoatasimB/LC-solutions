class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for second, first in prerequisites:
            adj[first].append(second)
        
        ans = []
        seen = [False for _ in range(numCourses)]
        cycle = False
        def dfs(node, currPath): 
            nonlocal cycle
            seen[node] = True
            currPath[node] = True
            for nei in adj[node]:
                if not seen[nei]:
                    dfs(nei,currPath)
                elif currPath[nei]:
                    cycle = True
            
            currPath[node] = False
            ans.append(node)
        
        for i in range(numCourses):
            if not seen[i]:
                dfs(i, [False for _ in range(numCourses)])
        return ans[::-1] if not cycle else []

            
