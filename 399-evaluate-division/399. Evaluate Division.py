class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            adj[a].append([b, val])
            adj[b].append([a, 1/val])

        
        def bfs(start, end):
            print("__________")
            if start not in adj:
                return -1
            seen = set()
            q = deque()
            q.append((start, 1))
            seen.add(start)
            while q:
                node, curr = q.popleft()
                print(node, curr)
                if node == end:
                    return curr

                for nei, val in adj[node]:
                    if nei not in seen:
                        seen.add(nei)
                        # curr = curr * val
                        q.append((nei, curr * val))
            return -1
        
        ans = []

        for start, end in queries:
            ans.append(bfs(start, end))
        
        return ans

        # adj = {
        #     X1 : [X2, 3],
        #     X2 : [X3, 4], [X1, 1/3]
        #     X3 : [X4, 5], [X2, 1/4]
        #     X4: [X5, 6], [X3, 1/5]
        #     X5: [X4, 1/6]
        # }

        # q = [x4,20] [x1,1/3] [x2, 4/3]