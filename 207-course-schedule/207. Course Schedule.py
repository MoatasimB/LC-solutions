class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        s = [False] * numCourses
        seen = [False] * numCourses

        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[y].append(x)
        

        def dfs(node):
            if s[node]:
                return True

            s[node] = True
            for nei in graph[node]:
                if s[nei]:
                    return True
                elif not seen[nei]:
                    seen[nei] = True
                    if dfs(nei):
                        return True
            s[node] = False
            return False
        

        for node in range(numCourses):
            if not seen[node]:
                seen[node] = True
                if dfs(node):
                    return False
        

        return True
