class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # graph = defaultdict(list)
        # for account in accounts:
        #     first_email = account[1]
        #     for i in range(2, len(account)):
        #         graph[first_email].append(account[i])
        #         graph[account[i]].append(first_email)

        
        # def dfs(node):
        #     seen.add(node)
        #     lst.append(node)
        #     for nei in graph[node]:
        #         if nei not in seen:
        #             dfs(nei)
        
        # seen = set()
        # final = []
        # for account in accounts:
        #     account_name = account[0]
        #     node = account[1]
        #     lst = [account_name]
        #     if node not in seen:
        #         dfs(node)
        #         lst[1:] = sorted(lst[1:])
        #         final.append(lst)

        # return final
  
        




        class UF:
            
            def __init__(self, size):
                self.roots = [i for i in range(size)]
                self.ranks = [0] * (size)
            
            def find(self, root):
                if self.roots[root] == root:
                    return root
                
                self.roots[root] = self.find(self.roots[root])

                return self.roots[root]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)

                if rootX != rootY:
                    if self.ranks[rootX] < self.ranks[rootY]:
                        self.roots[rootX] = rootY
                    elif self.ranks[rootX] > self.ranks[rootY]:
                        self.roots[rootY] = rootX
                    else:
                        self.roots[rootX] = rootY
                        self.ranks[rootX] += 1
            
        n = len(accounts)
        uf = UF(n)

        emails_to_idx = {}
        #Assign email to its respective idx -> email : i (0..len(accounts))
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email not in emails_to_idx:
                    emails_to_idx[email] = i
                else:
                    uf.union(i, emails_to_idx[email])
        
        components = defaultdict(list)
        #assign idx to its emails -> idx : [emails]
        for email, idx in emails_to_idx.items():
            components[uf.find(idx)].append(email)
        
        final = []

        for key, val in components.items():
            name = accounts[key][0]
            sorted_emails = sorted(val)
            final.append([name] + sorted_emails)

        return final