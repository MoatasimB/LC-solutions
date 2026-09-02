class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.o_set = set()
        self.x_set = set()

    def move(self, row: int, col: int, player: int) -> int:
        player_set = self.x_set if player == 1 else self.o_set
        player_set.add((row, col))
        return self.check(row, col, player)
        

        
    
    def check(self, row, col, player):
        player_set = self.x_set if player == 1 else self.o_set
        player_num = player
        #check neg diagonal
        count = 1
        count += self.checkDelta(row, col, 1, 1, player_set)
        count += self.checkDelta(row, col, -1, -1, player_set)
        if count == self.n:
            return player_num

        #check pos diagonal
        count = 1
        count += self.checkDelta(row, col, -1, 1, player_set)
        count += self.checkDelta(row, col, 1, -1, player_set)
        if count == self.n:
            return player_num

        
        
        #check horizontal
        count = 1
        count += self.checkDelta(row, col, 0, -1, player_set)
        count += self.checkDelta(row, col, 0, 1, player_set)
        if count == self.n:
            return player_num


        #check vertical
        count = 1
        count += self.checkDelta(row, col, 1, 0, player_set)
        count += self.checkDelta(row, col, -1, 0, player_set)
        if count == self.n:
            return player_num
        
        return 0
    
    def checkDelta(self, row, col, dx, dy, player_set):
        x, y = row + dx, col + dy
        count = 0
        while (x, y) in player_set:
            x += dx
            y += dy
            count += 1
        return count

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)