class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        

        graph = defaultdict(list)
        for account in accounts:
            for i in range(1, len(account)):
                for j in range(i+1, len(account)):
                    graph[account[i]].append(account[j])
                    graph[account[j]].append(account[i])
        
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            curr.append(node)
            if node in graph:
                for nei in graph[node]:
                    dfs(nei)

        ans = []
        seen = set()
        for account in accounts:
            name = account[0]
            head = account[1]
            curr = [name]
            if head not in seen:
                dfs(head)
                curr[1:] = sorted(curr[1:])
                ans.append(curr)
        

        return ans
