class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        def valid(r,c):
            return 0<=r<n and 0<=c<m
        seen = set()
        def check(r,c):
            curr = set()
            curr.add(matrix[r][c])
            seen.add((r,c))
            while valid(r,c):
                if matrix[r][c] not in curr:
                    return False
                seen.add((r,c))
                r += 1
                c += 1
            return True



        for r in range(n):
            for c in range(m):
                if (r,c) not in seen:
                    if not check(r,c):
                        return False
        
        return True
