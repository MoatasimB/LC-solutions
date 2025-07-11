class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        ans = []

        def dfs(i, curr):

            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for j in range(i,n+1):
                curr.append(j)
                dfs(j+1, curr)
                curr.pop()


        dfs(1, [])
        return ans