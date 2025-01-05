class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)

        for i in range(len(equations)):
            adj[equations[i][0]].append([equations[i][1], values[i]])
            adj[equations[i][1]].append([equations[i][0], 1/values[i]])
        print(adj)
        ans = []

        def dfs(currentNode,finalNode,curr,seen):

            # q = deque([(currentNode, curr)])
            
            # while q:
            #     node, currValue = q.popleft()

            #     if node == finalNode:
            #         return currValue
            #     seen.add(node)
            #     for nei,val in adj[node]:
            #         if nei not in seen:
            #             q.append((nei, currValue * val))
            
            # return -1





            if currentNode == finalNode:
                return curr
            seen.add(currentNode)
            ans = -1
            for nei,val in adj[currentNode]:
                if nei not in seen:
                    ans = dfs(nei, finalNode, curr*val, seen)
                    if ans != -1:
                        break

            
            return ans




        for start,end in queries:
            if (start not in adj) or (end not in adj):
                ans.append(-1.00000)
                continue
            ans.append(dfs(start, end, 1, set()))
        
        return ans
