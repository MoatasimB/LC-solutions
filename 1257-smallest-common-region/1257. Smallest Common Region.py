class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        graph = {}

        for lst in regions:
            start = lst[0]
            for node in lst[1:]:
                graph[node] = start


        parents = set()

        x = region1
        parents.add(x)
        y = region2
        while x in graph:
            x = graph[x]
            parents.add(x)
        
        
        if y in parents: return y
        while y in graph:
            
            y = graph[y]
            if y in parents:
                return y