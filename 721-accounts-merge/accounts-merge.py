class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = defaultdict(set)
        owners = {}
        for account in accounts:
            owner = account[0]
            for i in range(1, len(account)):
                if account[i] not in graph:
                    graph[account[i]] = set()
                owners[account[i]] = owner
                for j in range(i + 1, len(account)):
                    graph[account[i]].add(account[j])
                    graph[account[j]].add(account[i])

                    owners[account[j]] = owner

        
        def dfs(node):
            seen.add(node)
            lst.append(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
        
        seen = set()
        final = []
        for node, neighbors in graph.items():
            lst = []
            if node not in seen:
                dfs(node)
            if lst:
                final.append(lst)
        # print(final)
        ans = []
        for emails in final:
            # print(emails)
            owner = owners[emails[0]]
            # print(owner)
            sorted_emails = sorted(emails)
            ans.append([owner] + sorted_emails)
        
        return ans





        # class UF:
            
        #     def __init__(self, size):
        #         self.roots = [i for i in range(size)]
        #         self.ranks = [0] * len(size)
            
        #     def find(self, root):
        #         if self.roots = root:
        #             return root
                
        #         self.roots[root] = self.find(self.roots[root])

        #         return self.roots[root]
            
        #     def union(self, x, y):
        #         rootX = self.find(x)
        #         rootY = self.find(y)

        #         if rootX != rootY:
        #             if self.ranks[rootX] < self.ranks[rootY]:
        #                 self.roots[rootX] = rootY
        #             elif self.ranks[rootX] > self.ranks[rootY]:
        #                 self.roots[rootY] = rootX
        #             else:
        #                 self.roots[rootX] = rootY
        #                 self.ranks[rootX] += 1
            
