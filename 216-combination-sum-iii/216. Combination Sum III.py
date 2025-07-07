class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        

        ans = []

        def dfs(i, curr, goal):

            if len(curr) == k and goal == 0:
                ans.append(curr[:])
                return
            
            for j in range(i, 10):
                if goal - j >= 0:
                    curr.append(j)
                    dfs(j+1, curr, goal - j)
                    curr.pop()
        


        dfs(1, [], n)
        return ans