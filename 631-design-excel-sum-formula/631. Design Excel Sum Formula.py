class Excel:

    def __init__(self, height: int, width: str):
        width = ord(width) - ord("A") + 1
        self.mat = [[0] * width for _ in range(height)]
        self.depends = defaultdict(dict) #node : all the cells it depends on
        self.stack = []
    
    def getPos(self, row: int, column: str) -> List[int]:
        r = row - 1
        c = ord(column) - ord("A") 
        return [r, c]
    
    def applyChange(self, row: int, col: int) -> None:
        self.topo(row, col)
        self.calcStack()
    
    def topo(self, row: int, col: int) -> None:
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if (row, col) in self.depends[(i, j)]:
                    self.topo(i, j)
        self.stack.append((row, col))
    
    def calcStack(self) -> None:
        while self.stack:
            r, c = self.stack.pop()
            self.calc(r, c)
    
    def calc(self, r: int, c: int) -> None:
        if len(self.depends[(r, c)]) == 0:
            return
        self.mat[r][c] = 0
        for node, count in self.depends[(r, c)].items():
            nr, nc = node
            self.mat[r][c] += (self.mat[nr][nc] * count)


    def removePrev(self, r: int, c: int) -> None:
        self.depends[(r, c)] = {}

    def set(self, row: int, column: str, val: int) -> None:
        r, c = self.getPos(row, column)
        #when I set this value I no longer depend on any of those other nodes
        #I go through those nodes and remove the current node as a node that should get updated if one of those is updated
        self.removePrev(r, c)

        self.mat[r][c] = val
        self.applyChange(r, c)

    
    
    def get(self, row: int, column: str) -> int:
        r, c = self.getPos(row, column)

        return self.mat[r][c]
        

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        r, c = self.getPos(row, column)
        cells = defaultdict(int)
        for value in numbers:
            if ":" not in value:
                r1 = int(value[1:])
                c1 = value[0]
                p1, p2 = self.getPos(r1, c1)
                cells[(p1, p2)] += 1
            else:
                lst = value.split(":")
                topR = int(lst[0][1:])
                topC = lst[0][0]
                botR = int(lst[1][1:])
                botC = lst[1][0]
                tR, tC = self.getPos(topR, topC)
                bR, bC = self.getPos(botR, botC)

                for i in range(tR, bR + 1):
                    for j in range(tC, bC + 1):
                        cells[(i, j)] += 1
        total = 0
        self.removePrev(r, c)
        for key, count in cells.items():
            x, y = key
            total += self.mat[x][y] * count
            self.depends[(r, c)][(x, y)] =  count
        
        self.mat[r][c] = total
        self.applyChange(r, c)
        return self.mat[r][c]

        
  
#     A   B   C   D   E
# 1.  1

# 2.      0     

# 3

# 4

# 5
# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)