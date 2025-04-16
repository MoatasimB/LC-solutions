class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        ans = 0
        seen = set()
        def dfs(node):
            nonlocal ans

            seen.add(node)
            curr_max = 0
            prev = 0
            # curr = 0
            for nei in adj[node]:
                if nei in seen:
                    continue
                curr = 1 + dfs(nei)
                if curr > curr_max:
                    prev = curr_max
                    curr_max = curr
                elif curr > prev:
                    prev = curr
                ans = max(ans, curr_max + prev)
            
            return curr_max
        
        dfs(0)
        return ans


        