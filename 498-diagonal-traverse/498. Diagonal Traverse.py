class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:


        ans = []
        diagonals = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diagonals[r + c].append(mat[r][c])
        
        for i in range(r + c + 1):
            d = diagonals[i]
            if i % 2 == 0:
                for i in range(len(d) - 1, -1, -1):
                    ans.append(d[i])
            else:
                for i in range(len(d)):
                    ans.append(d[i])
        
        return ans
