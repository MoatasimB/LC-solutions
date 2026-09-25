class Node:
    def __init__(self, val, cellMap):
        self.val = val
        self.cellMap = cellMap

class Excel:

    def __init__(self, height: int, width: str):
        self.mat = [[Node(0, defaultdict(int)) for _ in range(ord(width) - ord("A") + 1)] for _ in range(height)]
        self.stack = []

    def set(self, row: int, column: str, val: int) -> None:
        column = ord(column) - ord("A")
        row -= 1
        node = self.mat[row][column]
        node.val = val
        node.cellMap = defaultdict(int)

        self.toposort(row, column, set())

        self.do_stack()
        

    def get(self, row: int, column: str) -> int:
        column = ord(column) - ord("A")
        row -= 1
        return self.mat[row][column].val



        

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        nums = self.get_nums(numbers)
        column = ord(column) - ord("A")
        row -= 1
        node = self.mat[row][column]

        node.val = 0
        node.cellMap = defaultdict(int)

        for r, c in nums:
            node.cellMap[(r, c)] += 1
        self.calculate_sum(row, column)
        self.toposort(r, c, set())
        self.do_stack()

        return node.val
        

    def get_nums(self, lst):
        ans = []

        for item in lst:
            if ":" not in item:
                row = int(item[1:]) - 1
                col = ord(item[0]) - ord("A")
                ans.append([row, col])
            else:
                start, end = item.split(":")
                startR, startC = int(start[1:]) - 1, ord(start[0]) - ord("A")
                endR, endC = int(end[1:]) - 1, ord(end[0]) - ord("A")

                for row in range(startR, endR + 1):
                    for col in range(startC, endC + 1):
                        ans.append([row, col])
        return ans
    
    def toposort(self,r, c, seen):
        if (r, c) in seen:
            return
        seen.add((r, c))

        for nr in range(len(self.mat)):
            for nc in range(len(self.mat[0])):
                node = self.mat[nr][nc]
                if (r, c) in node.cellMap:
                    self.toposort(nr, nc, set())
        self.stack.append([r, c])
    
    def do_stack(self):
        while self.stack:
            r, c = self.stack.pop()
            self.calculate_sum(r, c)
    
    def calculate_sum(self, r, c):
        total = 0
        node = self.mat[r][c]
        if len(node.cellMap) > 0:
            for cell, count in node.cellMap.items():
                nr = cell[0]
                nc = cell[1]
                total += self.mat[nr][nc].val * count
            self.mat[r][c].val = total

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)