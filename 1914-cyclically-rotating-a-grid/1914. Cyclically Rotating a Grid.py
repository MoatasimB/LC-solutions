class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])
        newGrid = [[0] * n for _ in range(m)]
        
        def rev(start, end, cells):
            while start < end:
                cells[start], cells[end] = cells[end], cells[start]
                start += 1
                end -= 1
        def applyRotation(sR, sC, eR, eC):
            cells = []
            # count how many cells in layer
            for i in range(sR, eR):
                cells.append(grid[i][sC])
            
            for i in range(sC, eC):
                cells.append(grid[eR][i])

            for i in range(eR, sR, -1):
                cells.append(grid[i][eC])
            
            for i in range(eC, sC, -1):
                cells.append(grid[sR][i])
            
            cell_len = len(cells)

            # mod by k
            rotations = k % cell_len
            
            # #apply rotation
            rev(0, cell_len - rotations - 1, cells)

            rev(cell_len - rotations,cell_len - 1, cells)

            

            rev(0, cell_len - 1, cells)

            # 30 20 10 40

            # 20 10 40 30
            idx = 0
            for i in range(sR, eR):
                newGrid[i][sC] = cells[idx]
                idx += 1
            
            for i in range(sC, eC):
                newGrid[eR][i] = cells[idx]
                idx += 1

            for i in range(eR, sR, -1):
                newGrid[i][eC] = cells[idx]
                idx += 1
            
            for i in range(eC, sC, -1):
                newGrid[sR][i] = cells[idx]
                idx += 1
            
            
        
        # [10, 6, 7, 11]
        row = 0
        col = 0

        # [1 16 .... 4 3 2]
        while row != (m // 2) and col != (n // 2):

            sR = row
            sC = col
            eR = m - row - 1
            eC = n - col - 1
            applyRotation(sR, sC, eR, eC)
           



            row += 1
            col += 1
        
        return newGrid

       