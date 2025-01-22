class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        matrix_indices = {}
        m = len(mat)
        n = len(mat[0])

        for r in range(m):
            for c in range(n):
                matrix_indices[mat[r][c]] = [r,c]
        
        rows = defaultdict(int)
        cols = defaultdict(int)

        for i in range(len(arr)):
            r,c = matrix_indices[arr[i]]
            rows[r] += 1
            cols[c] += 1

            if rows[r] == n:
                return i
            if cols[c] == m:
                return i
        

