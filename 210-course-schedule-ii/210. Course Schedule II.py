class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        adj = [[] for _ in range(numCourses)]
        
        
        for x, y in prerequisites:
            adj[y].append(x)
            
        seen = [False] * numCourses
        inStack = [False] * numCourses


        isPossible = True
        ans = []
        def dfs(node):
            nonlocal isPossible
            if not isPossible:
                return 
            
            if inStack[node]:
                isPossible = False
                return
            if seen[node]:
                return

            seen[node] = True
            inStack[node] = True

            for nei in adj[node]:
                dfs(nei)
                if not isPossible:
                    return
            
            ans.append(node)
            inStack[node] = False
        
        for i in range(numCourses):
            dfs(i)
        
        return ans[::-1] if len(ans) == numCourses else []

