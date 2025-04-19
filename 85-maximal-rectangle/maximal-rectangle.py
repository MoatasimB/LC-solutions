class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        def max_rec(row):

            stack = [] #idx, height
            ans = 0
            for i, height in enumerate(row):
                start = i
                while stack and int(stack[-1][1]) > int(height):
                    idx, h = stack.pop()
                    start = min(start, idx)
                    ans = max(ans,  (i - idx) * int(h))
                stack.append([start, height])

            while stack:
                idx, h = stack.pop()
                ans = max(ans, (m - idx) * int(h))
            
            return ans
        
        for c in range(len(matrix[0])):
            matrix[0][c] = int(matrix[0][c])
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):

                if int(matrix[i][j]) == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = int(matrix[i][j]) +  int(matrix[i-1][j])
        final = 0
        print(matrix)
        for row in matrix:
            final = max(final, max_rec(row))

        return final

# [["0","1","1","0","1"],
#  ["1","1","0","1","0"],
#  ["0","1","1","1","0"],
#  ["1","1","1","1","0"],
#  ["1","1","1","1","1"],
#  ["0","0","0","0","0"]]

# [[0, 1, 1, 0, 1], 
#  [1, 2, 0, 1, 0], 
#  [0, 3, 1, 2, 0], 
#  [1, 4, 2, 3, 0], 
#  [2, 5, 3, 4, 1], 
#  [0, 0, 0, 0, 0]]

#  ans = 6

#  (0,2), (1,3), (3, 4)

