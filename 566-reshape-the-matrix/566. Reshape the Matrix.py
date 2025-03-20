class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat
        

        new = [[0] * c for _ in range(r)]
        nums = [mat[i][j] for i in range(m) for j in range(n)]

        idx = 0
        for i in range(r):
            for j in range(c):
                new[i][j] = nums[idx]
                idx += 1

        return new

