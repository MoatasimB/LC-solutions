class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)

        for i in range(len(equations)):
            adj[equations[i][0]].append([equations[i][1], values[i]])
            adj[equations[i][1]].append([equations[i][0], 1/values[i]])
        print(adj)
        ans = []

        def bfs(currentNode,finalNode,curr,seen):

            q = deque([(currentNode, curr)])
            seen.add(currentNode)
            
            while q:
                node, currValue = q.popleft()

                if node == finalNode:
                    return currValue
                for nei,val in adj[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, currValue * val))
            
            return -1





            # if currentNode == finalNode:
            #     return curr
            # seen.add(currentNode)
            # for nei,val in adj[currentNode]:
            #     if nei not in seen:
            #         return dfs(nei, finalNode, curr*val, seen)
            
            # return -1.00000




        for start,end in queries:
            if (start not in adj) or (end not in adj):
                ans.append(-1.00000)
                continue
            ans.append(bfs(start, end, 1, set()))
        
        return ans
