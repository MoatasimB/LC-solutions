class Node:
    def __init__(self, val, cellMap):
        self.val = val
        self.cellMap = cellMap #[r,c] : count

class Excel:

    def __init__(self, height: int, width: str):
        self.grid = [
    [Node(0, defaultdict(int)) for _ in range(ord(width) - ord('A') + 1)]
    for _ in range(height)
]
        self.stack = []
 


    def set(self, row: int, column: str, val: int) -> None:

        row = row - 1
        col = ord(column) - ord('A')
        self.grid[row][col].val = val
        self.grid[row][col].cellMap = defaultdict(int)
        print("SETTED", row, col)

        self.topsort(row, col, set())
        print(self.stack)
        self.do_stack()


    def get(self, row: int, column: str) -> int:
        row = row - 1
        col = ord(column) - ord('A')
        return self.grid[row][col].val

        

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        nums = self.convert(numbers)
        row = row - 1
        col = ord(column) - ord('A')
        self.grid[row][col].cellMap = defaultdict(int)
        for r,c in nums:
            self.grid[row][col].cellMap[(r,c)] += 1
        print(self.grid[row][col].cellMap)
        self.calculate_sum(row, col)
        self.topsort(row, col, set())

        self.do_stack()

        return self.grid[row][col].val
            
        


    def convert(self, numbers):
        ans = []
        for key in numbers:
            if ':' not in key:
                r = int(key[1:]) - 1
                c = int(ord(key[0]) - ord('A'))
                ans.append([r,c])
            else:

                new_k = key.split(':')
    
                start_cell = new_k[0]
                end_cell = new_k[1]

                start_r = int(start_cell[1:]) - 1
                start_c = int(ord(start_cell[0]) - ord('A'))
                end_r = int(end_cell[1:]) - 1
                end_c = int(ord(end_cell[0]) - ord('A'))

                for i in range(start_r, end_r + 1):
                    for j in range(start_c, end_c + 1):
                        ans.append([i,j])
        return ans


    def topsort(self, r , c, visited):
        if (r,c) in visited:
            return
        visited.add((r,c))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                node = self.grid[i][j]
                if (r,c) in node.cellMap:
                    self.topsort(i, j, set())
        
        self.stack.append([r, c])
    
    def do_stack(self):
        while self.stack:
            r, c = self.stack.pop()
            if len(self.grid[r][c].cellMap) > 0:
                print("calculating")
                self.calculate_sum(r, c)
    
    def calculate_sum(self, r, c):
        node = self.grid[r][c]
        print("calc" , r, c)
        total = 0
        for cell, count in node.cellMap.items():
            nr = cell[0]
            nc = cell[1]
            print("toposort", nr, nc, self.grid[nr][nc].val)
            total += self.grid[nr][nc].val * count
        
        self.grid[r][c].val = total
        print( "new" , self.grid[r][c].val)
        return total

    

        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)